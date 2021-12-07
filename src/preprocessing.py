"""Process the protein sequence into specified data format for modeling.
"""
import pickle
import pandas as pd
# from utils import encode_data


def set_length_limit(df, length_limit=40, verbose=True):
    """Return sequences of length above specified length_limit.

    Args:
        df (dataframe): dataframe of protein sequence
        length_limit (int, optional): specified protein length limit.
            Defaults to 40.

    Returns:
        dataframe: sequences with length above specified length_limit
    """
    df.loc[:, 'length'] = df.loc[:, 'sequence'].map(lambda x: len(x))
    if verbose:
        print(f'Before setting length limit of {length_limit}: ')
        print(df.describe())
        print()
    else:
        pass
    df = df.loc[df.length >= length_limit]
    if verbose:
        print(f'After setting length limit of {length_limit}: ')
        print(df.describe())
        print()
    else:
        pass
    return df


def clean_disordered_sequence(infile_disordered):
    """Clean the disordered protein sequence.

    Args:
        infile_disordered ([str]): filename or path to the disordered protein
            sequence in csv format.

    Returns:
        dataframe: cleaned dataframe of disordered protein sequence.
    """
    df_disordered = pd.read_csv(infile_disordered)
    df_disordered = df_disordered[~df_disordered.sequence.isnull()]
    df_disordered = df_disordered.drop_duplicates()
    df_disordered = set_length_limit(df_disordered)
    return df_disordered


def clean_ordered_sequence(infile_ordered_1, infile_ordered_2):
    """Clean ordered protein sequence.

    Args:
        infile_ordered_1 (str): filename of ordered protein in csv format
        infile_ordered_2 (str): filename of ordered protein in csv format

    Returns:
        dataframe: cleaned sequence with lengh above specified length limit.
    """
    df1 = pd.read_csv(infile_ordered_1)
    df2 = pd.read_csv(infile_ordered_2)
    df_ordered = df1.append(df2)
    df_ordered = df_ordered.loc[:, ['Sequence']]
    df_ordered = df_ordered.rename(columns={'Sequence': 'sequence'})
    df_ordered = df_ordered[~df_ordered.sequence.isnull()]
    df_ordered = df_ordered.drop_duplicates()
    df_ordered = set_length_limit(df_ordered)
    return df_ordered


def save_processed_data(array_ordered, labels_ordered,
                        array_disordered, labels_disordered):
    """Save the processed data in a pickle format.

    Args:
        array_ordered (np.ndarray): three-dimensional array of features
            for ordered protein sequence
        labels_ordered (np.ndarray): one-dimensional array of labels
            for ordered protein sequence
        array_disordered (np.ndarray): three-dimensional array of features
            for disordered protein sequence
        labels_disordered (np.ndarray): one-dimensional array of labels
            for disordered protein sequence
    """
    dict_data = {
        "array_ordered": array_ordered,
        "labels_ordered": labels_ordered,
        "array_disordered": array_disordered,
        "labels_disordered": labels_disordered
    }
    with open("../data/protein_processed_data.pkl", "wb") as f_write:
        pickle.dump(dict_data, f_write)


# def main():
#     """Main.
#     """
#     infile_disordered = "disordered_sequences.csv"
#     infile_ordered_1 = \
#         "rcsb_pdb_sequence_9b20c2e6f4e2322c79be67683f6cf968_2501-3856.csv"
#     infile_ordered_2 = \
#         "rcsb_pdb_sequence_9b20c2e6f4e2322c79be67683f6cf968_0001-2500.csv"
#     df_disordered = clean_disordered_sequence(infile_disordered)
#     df_ordered = clean_ordered_sequence(infile_ordered_1, infile_ordered_2)
#     array_ordered, labels_ordered = encode_data(
#         df_ordered, 'ordered'
#     )
#     array_disordered, labels_disordered = encode_data(
#         df_disordered, 'disordered'
#     )
#     save_processed_data(
#         array_ordered, labels_ordered,
#         array_disordered, labels_disordered
#     )


# if __name__ == "__main__":
#     main()
