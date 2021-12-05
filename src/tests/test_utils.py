from collections import defaultdict
import pytest
import numpy as np
import pandas as pd
import os
import tensorflow as tf
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import utils
import preprocessing


LENGTH_LIMIT = 40


@pytest.fixture(name="input_data")
def example_data():
    sequences = [
        "LLGDFFRKSKEKIGKEFKRIVQRIKDFLRNLVPRTES",
        "MDAQTRRRERRAEKQAQWKAANPLLVGVSAKPVNRPILSLNRKPKSRVESALNPIDLTVLAEYHKQIESNLQRIERKNQTWYS",
        "MDAQTRRRERRAEKQAQWKAAN"]
    return sequences


@pytest.fixture(name="input_dataframe")
def example_dataframe():
    df = pd.DataFrame({"sequence": ['EHVIEMDVTSENGQRALKEQSSKAKIVKNRWGRNVVQISNT',
                                    'VYRNSRAQGGG',
                                    'MDAQTRRRERRAEKQAQWKAANPLLVGVSAKPVNRPILSLNRKPKS']})
    return df


def test_check_length(input_data):
    assert utils.check_length(input_data, LENGTH_LIMIT) is None


def test_check_protein_letters(input_data):
    assert utils.check_protein_letters(input_data) is None


def test_check_protein_letters_invalid():
    sequences = [
        "BDAQTRRRERRAEKQAQWKAANPLLVGVSAKPVNRPILSLNRKPKSRVESALNPIDLTVLAEYHKQIESNLQRIERKNQTWYB"
        ]
    with pytest.raises(TypeError):
        utils.check_protein_letters(sequences)


def test_check_data(input_data):
    assert utils.check_data(input_data, LENGTH_LIMIT) is None
    sequences = ["BDAQTRRRERRAEKQAQWKRVESALNPIDLTVLAEYHKQIESNLQRIERKNQTWYB"]
    with pytest.raises(TypeError):
        utils.check_data(sequences)


def test_generate_sub_sequence(input_dataframe):
    tmp = preprocessing.set_length_limit(input_dataframe)
    result = utils.generate_sub_sequence(tmp)
    assert isinstance(result, defaultdict)
    assert len(result.keys()) > 0



def test_one_hot_encoding(input_data):
    lst_sequences = ["MDAQTRRRERRAEKQAQWKAANPLLVGVSAKPVNRPILSL"]
    array = utils.one_hot_encoding(lst_sequences, LENGTH_LIMIT)
    assert isinstance(array, np.ndarray)
    assert len(array.shape) == 3
    with pytest.raises(IndexError):
        utils.one_hot_encoding(input_data, LENGTH_LIMIT)
    

def test_encode_data(input_dataframe):
    array_encoded, labels = utils.encode_data(input_dataframe)
    assert labels is None
    assert isinstance(array_encoded, np.ndarray)


def test_load_model():
    model = utils.load_model()
    assert isinstance(model, tf.keras.Sequential)
