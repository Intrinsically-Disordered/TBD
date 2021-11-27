import pandas as pd
import numpy as np
import pickle


UNIQUE_LETTERS = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
                  'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
UNIQUE_LETTERS = np.array(UNIQUE_LETTERS)


def set_length_limit(df, length_limit=40):
    """Return sequences of length above specified length_limit."""
    df.loc[:, 'length'] = df.loc[:, 'sequence'].map(lambda x: len(x))
    print(f'Before setting length limit of {length_limit}: ')
    print(df.describe())
    print()
    df = df.loc[df.length >= length_limit]
    print(f'After setting length limit of {length_limit}: ')
    print(df.describe())
    return df


def clean_disordered_sequence(infile_disordered):
    df_disordered = pd.read_csv(infile_disordered)
    df_disordered = df_disordered[~df_disordered.sequence.isnull()]
    df_disordered = df_disordered.drop_duplicates()
    df_disordered = set_length_limit(df_disordered)
    return df_disordered


def clean_ordered_sequence(infile_ordered_1, infile_ordered_2):
    df1 = pd.read_csv()
    df2 = pd.read_csv()
    df_ordered = df1.append(df2)
    df_ordered = df_ordered.loc[:, ['Sequence']]
    df_ordered = df_ordered.rename(columns={'Sequence': 'sequence'})
    df_ordered = df_ordered[~df_ordered.sequence.isnull()]
    df_ordered = df_ordered.drop_duplicates()
    df_ordered = set_length_limit(df_ordered)
    return df_ordered


def generate_sub_sequence(df, size=40, strides=10):
    """Generate sub-sequence of specified size. 
       Moving at specified strides"""
    lst = []
    for sequence in df.sequence.values:
        for ix in range((len(sequence)-size)//strides+1):
            sub = sequence[strides*ix: strides*ix+size]
            lst.append(sub)
    return lst


def one_hot_encoding(df, protein_type, size=40, strides=10):
    """One-hot encoding the sequences.
       protein_type should be one of ['ordered', 'disordered']"""
    lst_sequences = generate_sub_sequence(df, size=size, strides=strides)
    num_obs = len(lst_sequences)
    # placeholder
    array_encoded = np.empty((num_obs, size, len(UNIQUE_LETTERS)))
    for ix, sequence in enumerate(lst_sequences):
        for iy, letter in enumerate(sequence):
            array_encoded[ix, iy, ] = (UNIQUE_LETTERS == letter).astype(int)
    if protein_type == 'ordered':
        labels = np.array([1]*num_obs)
    elif protein_type == 'disordered':
        labels = np.array([0]*num_obs)
    else:
        raise Exception(f"Invalid type: {protein_type}")
    return array_encoded, labels


def save_processed_data(array_ordered, labels_ordered, array_disordered, labels_disordered):
    with open("array_ordered.pkl", "wb") as f_write:
        pickle.dump(array_ordered, f_write)

    with open("labels_ordered.pkl", "wb") as f_write:
        pickle.dump(labels_ordered, f_write)

    with open("array_disordered.pkl", "wb") as f_write:
        pickle.dump(array_disordered, f_write)

    with open("labels_disordered.pkl", "wb") as f_write:
        pickle.dump(labels_disordered, f_write)


def main():
    infile_disordered = "disordered_sequences.csv"
    infile_ordered_1 = "rcsb_pdb_sequence_9b20c2e6f4e2322c79be67683f6cf968_2501-3856.csv"
    infile_ordered_2 = "rcsb_pdb_sequence_9b20c2e6f4e2322c79be67683f6cf968_0001-2500.csv"
    df_disordered = clean_disordered_sequence(infile_disordered)
    df_ordered = clean_ordered_sequence(infile_ordered_1, infile_ordered_2)
    array_ordered, labels_ordered = one_hot_encoding(df_ordered, 'ordered')
    array_disordered, labels_disordered = one_hot_encoding(
        df_disordered, 'disordered'
    )
    save_processed_data(array_ordered, labels_ordered,
                        array_disordered, labels_disordered)


if __name__ == "__main__":
    main()
