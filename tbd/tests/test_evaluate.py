from tbd.model import load_data
from tbd.utils import load_model
from tbd.evaluate import evaluate_model


def test_evaluate_model():
    model = load_model()
    data_infile = 'data/protein_processed_data.pkl'
    X_train, X_test, y_train, y_test = load_data(data_infile)
    assert evaluate_model(model, X_test, y_test) is None
