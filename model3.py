import pickle
import numpy as np

with open("prediction/model.pkl", "rb") as f:
    model = pickle.load(f)


def Predict(B, C, Cr, Cu, Fe, Mn, Mo, Ni, P, S, Si, Ti, V, W, Zn) -> float:
    input_vector = np.array([
        [0, 0, B, C, 0, 0, 0, Cr, Cu, Fe, 0, 0, Mn, Mo, 0, 0, Ni, 0, P, 0, S, 0, Si, 0, 0, Ti, V, W, Zn, 0]
    ])
    prediction = model.predict(input_vector)
    return prediction[0]
