from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression

# Build and train model at runtime (small + fast)
X, y = make_regression(n_samples=100, n_features=2, noise=0.1, random_state=42)
model = RandomForestRegressor(n_estimators=10, random_state=42)
model.fit(X, y)

def predict(compound: str, protein: str):
    # Fake feature extraction: use string lengths
    features = [[len(compound), len(protein)]]
    score = model.predict(features)[0]
    return {"binding_score": round(score, 3)}
