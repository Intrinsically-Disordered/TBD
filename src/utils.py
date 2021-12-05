"""Utility functions."""
from collections import defaultdict
import numpy as np
import pandas as pd
import tensorflow as tf


# Unique letters of protein sequences.
UNIQUE_LETTERS = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
                  'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
UNIQUE_LETTERS = np.array(UNIQUE_LETTERS)


def check_length(lst, length_limit):
    """Check the length of the input protein sequence.

    Args:
        lst (list): protein sequences in a list
        length_limit (int): specified protein length limit.
    """    
    for seq in lst:
        if len(seq) < length_limit:
            print(f"The sequence {seq} is less than "
                  "the specified length limit {length_limit}")
        else:
            pass


def check_protein_letters(lst):
    """Check the letters of protein sequence.

    Args:
        lst (list): protein sequences in a list
    """    
    for seq in lst:
        for letter in seq:
            if letter not in UNIQUE_LETTERS:
                print(f"The sequence {seq} contains invalid letters.")
            else:
                continue


def check_data(data, length_limit):
    """Check the input data.

    Args:
        data (list of pd.DataFrame): input data as a list or dataframe
        length_limit (int): specified protein length limit.

    Raises:
        TypeError: raise an exception if the input data don't have the right type.
    """    
    if isinstance(data, list):
        pass
    elif isinstance(data, pd.DataFrame):
        lst = list(data.sequence.values)
    else:
        raise TypeError(f"Invalid data type!")
    check_length(lst, length_limit)
    check_protein_letters(lst)


def generate_sub_sequence(df, size=40, strides=10):
    """Generate sub-sequence of specified size. Moving at specified strides

    Args:
        df (dataframe): [description]
        size (int, optional): specified protein length limit. Defaults to 40.
        strides (int, optional): length of strides with which to extract the sequence.
            Defaults to 10.

    Returns:
        list: a list of sequences with specified size.
    """
    lst = defaultdict(list)
    for sequence in df.sequence.values:
        for ix in range((len(sequence)-size)//strides+1):
            sub = sequence[strides*ix: strides*ix+size]
            lst[sequence].append(sub)
    return lst


def one_hot_encoding(lst_sequences, length_limit):
    """One-hot encoding the sequences.

    Args:
        lst_sequences (list): a list of sub_sequences with length of `length_limit`
        length_limit (int): specified protein length limit. Defaults to 40.

    Returns:
        np.ndarrary: the array after one-hot encoding.
    """    
    num_obs = len(lst_sequences)
    # placeholder
    array_encoded = np.empty((num_obs, size, len(UNIQUE_LETTERS)))
    for ix, sequence in enumerate(lst_sequences):
        for iy, letter in enumerate(sequence):
            array_encoded[ix, iy, ] = (UNIQUE_LETTERS == letter).astype(int)
    return array_encoded


def encode_data(df, protein_type=None, size=40, strides=10):
    """One-hot encoding the sequences. protein_type should be
       one of ['ordered', 'disordered']

    Args:
        df (dataframe): [description]
        protein_type (str, optional): one of ['ordered', 'disordered', None]
        size (int, optional): specified protein length limit. Defaults to 40.
        strides (int, optional): length of strides with which to extract the sequence.
            Defaults to 10.

    Raises:
        Exception: raise exception if the protein_type is not correct.

    Returns:
        numpy.ndarray: three-dimensional array of one-hot-encoding for features
            (num_obs, size, len(UNIQUE_LETTERS))
        numpy.ndarray: one-dimensional array of labels
    """
    sub_sequences = generate_sub_sequence(df, size=size, strides=strides)
    lst_sequences = list(sub_sequences.values())[0]
    array_encoded = one_hot_encoding(lst_sequences, size)
    if protein_type == 'ordered':
        labels = np.array([1]*num_obs)
    elif protein_type == 'disordered':
        labels = np.array([0]*num_obs)
    else:
        labels = None
    return array_encoded, labels


def load_model(infile="fitted_model"):
    """Load fitted model.

    Args:
        infile (str, optional): path to saved model. Defaults to "fitted_model".

    Returns:
        model: fitted model.
    """
    model = tf.keras.models.load_model(infile)
    return model
