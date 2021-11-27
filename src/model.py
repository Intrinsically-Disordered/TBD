"""
Model to classifiy protein sequence as ordered or disordered.
"""
import pdb
import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator


def load_data(infile):
    """Load data array.

    Args:
        infile (str): path to file

    Returns:
        pickle: loaded pickle object for data.
    """
    with open(infile, 'rb') as f_read:
        obj = pickle.load(f_read)
    array_ordered = obj["array_ordered"]
    labels_ordered = obj["labels_ordered"]
    array_disordered = obj["array_disordered"]
    labels_disordered = obj["labels_disordered"]
    return array_ordered, labels_ordered, array_disordered, labels_disordered


def augment_data(features, labels, num_times=6):
    """Augment the data by randomly sampling `num_times` times.

    Args:
        features (np.ndarray): three-dimensional array
        labels (np.ndarray): one-dimensional array
        num_times (int, optional): the number of times of samples. Defaults to 6.

    Returns:
        np.ndarray: three-dimensional and one-dimensional array after being augmented.
    """
    num_obs = features.shape[0]
    np.random.seed(10086)
    # Randomly sample num_times the number of observations
    random_index = np.random.randint(0, num_obs, num_obs*num_times)
    features_sampled = features[random_index]
    features_augmented = np.vstack([features, features_sampled])
    labels_sampled = labels[random_index]
    labels_augmented = np.hstack([labels, labels_sampled])
    return features_augmented, labels_augmented


def combine_ordered_disordered(array_ordered, labels_ordered,
                               array_disordered, labels_disordered):
    """Combine the ordered and disordered data into one array

    Args:
        array_ordered (np.ndarray): three-dimensional array of ordered protein
        labels_ordered (np.ndarray): one-dimensional array of ordered protein labels
        array_disordered (np.ndarray): three-dimensional array of disordered protein
        labels_disordered (np.ndarray): one-dimensional array of disordered protein labels

    Returns:
        np.ndarray: [description]
    """
    ## For dev only
    array_ordered = array_ordered[:array_disordered.shape[0]]
    labels_ordered = labels_ordered[:array_disordered.shape[0]]
    ###
    features = np.vstack([array_ordered, array_disordered])
    labels = np.hstack([labels_ordered, labels_disordered])
    return features, labels


def fit_model(X_train, X_test, y_train, y_test):
    """Fit a CNN model.

    Args:
        X_train (np.ndarrary): features of training data
        X_test (np.ndarrary): features of test data
        y_train (np.ndarrary): labels of training data
        y_test (np.ndarrary): labels of test data

    Returns:
        model: Fitted CNN model
    """    
    model = tf.keras.Sequential()
    model.add(tf.keras.Input(shape=(40, 20, 1)))
    model.add(tf.keras.layers.Conv2D(16, 2, strides=2, activation='relu'))
    model.add(tf.keras.layers.MaxPooling2D(2, strides=2))
    model.add(tf.keras.layers.Conv2D(8, 2, strides=2, activation='relu'))
    model.add(tf.keras.layers.MaxPooling2D(2, strides=2))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(16, activation='relu'))
    model.add(tf.keras.layers.Dense(2, activation='softmax'))
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
                  loss=tf.keras.losses.CategoricalCrossentropy(),
                  metrics=[tf.keras.metrics.CategoricalAccuracy(), tf.keras.metrics.AUC()])
    model.fit(X_train, y_train, steps_per_epoch=len(X_train)//4, epochs=8,
              validation_data=(X_test, y_test), validation_steps=int(len(X_test)/5))
    print(model.summary())
    return model


def main():
    """Main.
    """    
    infile = "../data/protein_processed_data.pkl"
    array_ordered, labels_ordered, array_disordered, labels_disordered = \
        load_data(infile)
    array_disordered_augmented, labels_disordered_augmented = \
        augment_data(array_disordered, labels_disordered, num_times=1)
    features, labels = combine_ordered_disordered(
        array_ordered, labels_ordered, array_disordered_augmented, labels_disordered_augmented
    )
    features = features.reshape((len(features), 40, 20, 1))
    labels = tf.keras.utils.to_categorical(labels)
    X_train, X_test, y_train, y_test = train_test_split(
        features, labels, test_size=0.2, random_state=110
    )
    model = fit_model(X_train, X_test, y_train, y_test)


if __name__ == "__main__":
    main()
