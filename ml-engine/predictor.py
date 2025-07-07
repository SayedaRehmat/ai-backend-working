import joblib
import os

model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
model = joblib.load(model_path)

def predict(compound: str, protein: str):
    features = [[len(compound), len(protein)]]
    score = model.predict(features)[0]
    return {"binding_score": round(score, 3)}
