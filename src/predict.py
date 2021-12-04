from collections import defaultdict
import pandas as pd
from preprocessing import set_length_limit
from utils import generate_sub_sequence, encode_data


def features_as_df(df):
    """Put original sequence and sub-sequence in a dataframe, 
       with one column as original sequence and another column as
       subsequence.

    Args:
        df (pd.dataframe): Dataframe with one column of inputted protein sequences.

    Raises:
        Exception: If all inputted sequences are shorter than specified length limit
                   then raise exception.
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
    if isinstance(data, list):
        df = pd.DataFrame(data, columns=['sequence'])
    elif isinstance(data, pd.DataFrame):
        lst = list(data.sequence.values)
    else:
        raise TypeError(f"Invalid data type!")
    df = set_length_limit(df, verbose=verbose)
    df_features = features_as_df(df)
    features, _ = encode_data(df)
    shapes = features.shape
    arrary_features = features.reshape((shapes[0], shapes[1], shapes[2], 1))
    return arrary_features, df_features
