"""Example to predict the protein sequence as ordered or disordered."""
from predict import transform_data, predict


sequences = ["LLGDFFRKSKEKIGKEFKRIVQRIKDFLRNLVPRTES",
             "MDAQTRRRERRAEKQAQWKAANPLLVGVSAKPVNRPILSLNRKPKSRVESALNPIDLTVLAEYHKQIESNLQRIERKNQTWYSKPGERGITCSGRQKIKGKSIPLI",
             "MDAQTRRRERRAEKQAQWKAAN"]
df_pred = predict(sequences)
print(df_pred)
