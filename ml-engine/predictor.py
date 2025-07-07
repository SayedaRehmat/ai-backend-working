from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression

# Train small model every time app starts
X, y = make_regression(n_samples=100, n_features=2, noise=0.1, random_state=42)
model = RandomForestRegressor(n_estimators=10, random_state=42)
model.fit(X, y)

def predict(compound: str, protein: str):
    features = [[len(compound), len(protein)]]
    score = model.predict(features)[0]
    return {"binding_score": round(score, 3)}
