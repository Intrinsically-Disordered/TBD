import evaluate
import model
import preprocessing
import utils

# Process data
infile_disordered = "data/disordered_sequences.csv"
infile_ordered_1 = \
    "data/rcsb_pdb_sequence_9b20c2e6f4e2322c79be67683f6cf968_2501-3856.csv"
infile_ordered_2 = \
    "data/rcsb_pdb_sequence_9b20c2e6f4e2322c79be67683f6cf968_0001-2500.csv"
df_disordered = preprocessing.clean_disordered_sequence(infile_disordered)
df_ordered = preprocessing.clean_ordered_sequence(infile_ordered_1, 
	infile_ordered_2)
array_ordered, labels_ordered = utils.encode_data(
    df_ordered, 'ordered'
)
array_disordered, labels_disordered = utils.encode_data(
    df_disordered, 'disordered'
)

# Save processed data
processed_file = "data/protein_processed_data.pkl"
preprocessing.save_processed_data(
    array_ordered, labels_ordered,
    array_disordered, labels_disordered,
    processed_file
)

# Fit model
X_train, X_test, y_train, y_test = model.load_data(processed_file)
model = model.fit_model(X_train, X_test, y_train, y_test)
model.save('fitted_model_test')

# Evaluate model
model = utils.load_model()
evaluate.evaluate_model(model, X_test, y_test)
