import os
import joblib

MODEL_PATH = os.path.join("models", "model.pkl")
model = joblib.load(MODEL_PATH)
print(model.predict([[5.1, 3.5, 1.4, 0.2]]))



