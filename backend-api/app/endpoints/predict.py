from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../ml-engine")))
from predictor import predict as ml_predict

router = APIRouter()

class PredictionInput(BaseModel):
    compound: str
    protein: str

@router.post("/predict")
def predict(input: PredictionInput) -> Dict:
    result = ml_predict(input.compound, input.protein)
    return {
        "compound": input.compound,
        "protein": input.protein,
        "binding_score": result["binding_score"]
    }
