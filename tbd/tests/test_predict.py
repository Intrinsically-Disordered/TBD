import pytest
import numpy as np
import pandas as pd
from tbd.predict import features_as_df,\
    transform_data,\
    predict_protein


@pytest.fixture(name='input_data')
def example_data():
    sequences = [
        'LLGDFFRKSKEKIGKEFKRIVQRIKDFLRNLVPRTES',
        'MDAQTRRRERRAEKQAQWKAANPLLVGVSAKPVNRPIL'
        'SLNRKPKSRVESALNPIDLTVLAEYHKQIESNLQRIERKNQTWYS',
        'MDAQTRRRERRAEKQAQWKAAN']
    return sequences


@pytest.fixture(name='input_dataframe')
def example_dataframe(input_data):
    df = pd.DataFrame(input_data, columns=['sequence'])
    return df


def test_features_as_df(input_dataframe):
    df_seq = features_as_df(input_dataframe)
    assert isinstance(df_seq, pd.DataFrame)
    assert len(df_seq) > 0
    assert 'parent_sequence' in df_seq.columns
    assert 'sequence' in df_seq.columns


def test_transform_data(input_data):
    arrary_features, df_features = transform_data(input_data)
    assert isinstance(arrary_features, np.ndarray)
    assert isinstance(df_features, pd.DataFrame)
    assert len(arrary_features.shape) == 4


def test_predict_protein(input_data):
    df_pred = predict_protein(input_data)
    assert isinstance(df_pred, pd.DataFrame)
    assert len(df_pred) > 0
