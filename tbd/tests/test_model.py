import os
import numpy as np
import pytest
from tbd.model import load_data,\
    augment_data,\
    combine_ordered_disordered


@pytest.fixture(name='array_ordered')
def features_ordered():
    array = np.array([[[0, 2],
                       [2, 0],
                       [0, 0]],

                      [[0, 4],
                       [1, 3],
                       [0, 1]]])
    return array


@pytest.fixture(name='array_disordered')
def features_disordered():
    array = np.array([[[1, 1],
                       [3, 3],
                       [3, 3]],

                      [[3, 2],
                       [1, 3],
                       [1, 2]]])
    return array


@pytest.fixture(name='labels_ordered')
def outcome_ordered():
    array = np.array([1, 0])
    return array


@pytest.fixture(name='labels_disordered')
def outcome_disordered():
    array = np.array([1, 1])
    return array


def test_load_data():
    parent_dir = os.path.abspath(os.path.join(
        os.path.dirname(__file__), './data'))
    infile = os.path.join(parent_dir, 'protein_processed_data.pkl')
    array_ordered, labels_ordered, array_disordered, labels_disordered = \
        load_data(infile)
    assert isinstance(array_ordered, np.ndarray)
    assert isinstance(labels_ordered, np.ndarray)
    assert isinstance(array_disordered, np.ndarray)
    assert isinstance(labels_disordered, np.ndarray)


def test_augment_data(array_disordered, labels_disordered):
    num_times = 4
    features_augmented, labels_augmented = augment_data(
        array_disordered, labels_disordered, num_times=num_times
    )
    assert features_augmented.shape[0] == \
        (1 + num_times) * array_disordered.shape[0]
    assert labels_augmented.shape[0] == \
        (1 + num_times) * labels_disordered.shape[0]


def test_combine_ordered_disordered(array_ordered, labels_ordered,
                                    array_disordered, labels_disordered):
    features, labels = combine_ordered_disordered(
        array_ordered, labels_ordered,
        array_disordered, labels_disordered
    )
    assert features.shape[0] == \
        array_ordered.shape[0] + array_disordered.shape[0]
    assert labels.shape[0] == \
        labels_ordered.shape[0] + labels_disordered.shape[0]
