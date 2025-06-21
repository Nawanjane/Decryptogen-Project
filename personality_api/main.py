from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import pickle
import os
import joblib
import pandas as pd

MODELS_DIR = os.path.join(os.path.dirname(__file__), 'modles')

app = FastAPI(
    title="Personality Prediction API",
    description="API for predicting personality type (Introvert/Extrovert)",
    version="1.0.0"
)

try:
    model = load_model(os.path.join(MODELS_DIR, 'best_model.h5'))
    with open(os.path.join(MODELS_DIR, 'scaler.pkl'), 'rb') as f:
        scaler = pickle.load(f)
except Exception as e:
    print(f"Error loading model or scaler: {e}")
    raise

class PersonalityInput(BaseModel):
    time_spent_alone: float
    social_event_attendance: float
    going_outside: float
    friends_circle_size: float
    post_frequency: float
    stage_fear: bool
    drained_after_socializing: bool

    class Config:
        schema_extra = {
            "example": {
                "time_spent_alone": 7.5,
                "social_event_attendance": 2.0,
                "going_outside": 3.0,
                "friends_circle_size": 5.0,
                "post_frequency": 2.0,
                "stage_fear": True,
                "drained_after_socializing": True
            }
        }

def predict_personality_rf(input_dict):
    
    # Load saved model and encoder
    model = joblib.load(os.path.join(MODELS_DIR, "rf_personality_model.pkl"))
    le_personality = joblib.load(os.path.join(MODELS_DIR, "le_personality.pkl"))
    scaler = joblib.load(os.path.join(MODELS_DIR, "scaler.pkl"))

    # Mapping of input dictionary keys to expected feature names
    feature_mapping = {
        'time_spent_alone': 'Time_spent_Alone',
        'social_event_attendance': 'Social_event_attendance',
        'going_outside': 'Going_outside',
        'friends_circle_size': 'Friends_circle_size',
        'post_frequency': 'Post_frequency',
        'stage_fear': 'Stage_fear_encoded',
        'drained_after_socializing': 'Drained_after_socializing_encoded'
    }

    # Prepare input DataFrame with correct column names
    df_input = pd.DataFrame([{feature_mapping[key]: value for key, value in input_dict.items()}])

    # Encode boolean features to match training data
    df_input['Stage_fear_encoded'] = df_input['Stage_fear_encoded'].astype(int)
    df_input['Drained_after_socializing_encoded'] = df_input['Drained_after_socializing_encoded'].astype(int)

    # Ensure the order of columns matches the training data
    selected_features = ['Time_spent_Alone', 'Social_event_attendance', 'Going_outside', 'Friends_circle_size', 'Post_frequency', 'Stage_fear_encoded', 'Drained_after_socializing_encoded']
    df_input = df_input[selected_features]

    # Scale the input features
    input_scaled = scaler.transform(df_input)

    # Predict
    probs = model.predict_proba(input_scaled)[0]
    pred_index = np.argmax(probs)
    pred_label = le_personality.inverse_transform([pred_index])[0]
    confidence = float(probs[pred_index])

    return {
        "personality": pred_label,
        "confidence": confidence,
        "status": "success"
    }

@app.post("/predict", response_model=dict)
async def predict_personality(data: PersonalityInput):
    try:
        input_dict = data.dict()
        result = predict_personality_rf(input_dict)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {
        "message": "Personality Prediction API",
        "docs": "/docs",
        "health": "OK"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}