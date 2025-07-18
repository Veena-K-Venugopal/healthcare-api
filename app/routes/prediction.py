from fastapi import APIRouter
from pydantic import BaseModel
from app.services.mock_model import predict
from app.services.enhancer import enhance_prediction_output

router = APIRouter()

class InputData(BaseModel):
    name: str
    age: int
    symptom: str

@router.post("/predict")
def get_prediction(data: InputData):
    result = predict(data)
    enhanced_result = enhance_prediction_output(result)
    return enhanced_result