from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="Startup Profit Prediction API")

model = joblib.load("model.pkl")


class StartupData(BaseModel):
    rd_spend: float
    administration: float
    marketing_spend: float
    state_florida: int
    state_new_york: int


@app.get("/")
def home():
    return {
        "message": "Startup Profit Prediction API is Running"
    }


@app.post("/predict")
def predict(data: StartupData):

    features = np.array([
        [
            data.rd_spend,
            data.administration,
            data.marketing_spend,
            data.state_florida,
            data.state_new_york
        ]
    ])

    prediction = model.predict(features)

    return {
        "predicted_profit": float(prediction[0])
    }