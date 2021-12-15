import os
import numpy as np
import pytest
import pandas as pd
from tbd.preprocessing import set_length_limit,\
    clean_disordered_sequence,\
    clean_ordered_sequence


@pytest.fixture(name='input_data')
def example_data():
    df = pd.DataFrame({
        'sequence':
            ['EHVIEMDVTSENGQRALKEQSSKAKIVKNRWGRNVVQISNT',
             'VYRNSRAQGGG',
             'MDAQTRRRERRAEKQAQWKAANPLLVGVSAKPVNRPILSLNRKPKS']
    })
    return df


def test_set_length_limit(input_data):
    result = set_length_limit(input_data)
    expected = pd.DataFrame({
        'sequence':
            ['EHVIEMDVTSENGQRALKEQSSKAKIVKNRWGRNVVQISNT',
             'MDAQTRRRERRAEKQAQWKAANPLLVGVSAKPVNRPILSLNRKPKS'],
        'length': [41, 46]
    })
    assert np.array_equal(result.values, expected.values)


def test_clean_disordered_sequence():
    parent_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../..')
    )
    infile_disordered = os.path.join(
        parent_dir, 'data/disordered_sequences.csv'
    )
    assert isinstance(
        clean_disordered_sequence(infile_disordered),
        pd.DataFrame
    )


def test_clean_ordered_sequence():
    parent_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../..')
    )
    infile_ordered_1 = os.path.join(
        parent_dir,
        'data/rcsb_pdb_sequence_9b20c2e6f4e2322c79be67683f6cf968_2501-3856.csv'
    )
    infile_ordered_2 = os.path.join(
        parent_dir,
        'data/rcsb_pdb_sequence_9b20c2e6f4e2322c79be67683f6cf968_0001-2500.csv'
    )
    assert isinstance(
        clean_ordered_sequence(infile_ordered_1, infile_ordered_2),
        pd.DataFrame
    )
