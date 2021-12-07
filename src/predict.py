"""Functions related to the model prediction."""
import pandas as pd
from preprocessing import set_length_limit
from utils import generate_sub_sequence, encode_data, load_model


def features_as_df(df):
    """Put original sequence and sub-sequence in a dataframe,
       with one column as original sequence and another column as
       subsequence.

    Args:
        df (pd.dataframe): Dataframe with one column of
            inputted protein sequences.

    Raises:
        Exception: If all inputted sequences are shorter than
            specified length limit then raise exception.
    Returns:
        df: dataframe with two columns, one column is the original sequence
            and another column is subsequence
    """
    sub_sequences = generate_sub_sequence(df)
    lst = []
    for key, value in sub_sequences.items():
        length = len(value)
        parent_seq = key * length
        df_seq = pd.DataFrame(
            {'parent_sequence': parent_seq, 'sequence': value}
        )
        lst.append(df_seq)
    if len(lst) == 0:
        raise Exception(
            "All inputted sequences are less than specified length limit.")
    else:
        df_seq = pd.concat(lst)
    return df_seq


def transform_data(data, verbose=False):
    """Transform the input data to be used by prediction.

    Args:
        data (list or dataframe): Input data in a list or
            dataframe with column name `sequence`.
        verbose (bool, optional): Whether to print out statistics
            of input protein sequence. Defaults to False.

    Raises:
        TypeError: Exception wil be raised in the input data
            don't have the right type.

    Returns:
        np.ndarray: Transformed features of the input data in an array
        pd.DataFrame: Dataframe that contain both the parent sequence
            and the sub-sequences.
    """
    if isinstance(data, list):
        data = pd.DataFrame(data, columns=['sequence'])
    elif isinstance(data, pd.DataFrame):
        pass
    else:
        raise TypeError("Invalid data type!")
    df = set_length_limit(data, verbose=verbose)
    df_features = features_as_df(df)
    features, _ = encode_data(df)
    shapes = features.shape
    arrary_features = features.reshape((shapes[0], shapes[1], shapes[2], 1))
    return arrary_features, df_features


def predict_protein(data):
    """Predict the protein sequence.

    Args:
        data (np.ndarray): input data in an array after one-hot-encoding

    Returns:
        pd.DataFrame: the prediction results for each sub-sequences.
    """
    model = load_model()
    features, df_features = transform_data(data)
    predictions = model.predict(features)
    df_pred = pd.DataFrame(
        predictions, columns=['prob_disordered', 'prob_ordered']
        )
    df_pred = df_features.join(df_pred)
    return df_pred
