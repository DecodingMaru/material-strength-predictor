import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

data = pd.read_csv("/data/Alloys.csv")

X = data.drop(["Alloy", "Tensile Strength: Ultimate (UTS) (psi)", "Melting Completion (Liquidus)"], axis=1)
y = data["Tensile Strength: Ultimate (UTS) (psi)"]

# Training model
model = RandomForestRegressor()
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

