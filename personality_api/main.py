# Import required libraries
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import pickle
import os

# Get the absolute path to the models directory
MODELS_DIR = os.path.join(os.path.dirname(__file__), 'modles')

# Initialize FastAPI app
app = FastAPI(
    title="Personality Prediction API",
    description="API for predicting personality type (Introvert/Extrovert)",
    version="1.0.0"
)

# Load model and scaler
try:
    model = load_model(os.path.join(MODELS_DIR, 'best_model.h5'))
    with open(os.path.join(MODELS_DIR, 'scaler.pkl'), 'rb') as f:
        scaler = pickle.load(f)
except Exception as e:
    print(f"Error loading model or scaler: {e}")
    raise

# Define input data model
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

# Define prediction endpoint
@app.post("/predict", response_model=dict)
async def predict_personality(data: PersonalityInput):
    try:
        # Convert input to array
        input_data = np.array([[
            data.time_spent_alone,
            data.social_event_attendance,
            data.going_outside,
            data.friends_circle_size,
            data.post_frequency,
            int(data.stage_fear),
            int(data.drained_after_socializing)
        ]])
        
        # Scale the input
        input_scaled = scaler.transform(input_data)
        
        # Make prediction
        prediction = model.predict(input_scaled)
        personality_type = "Introvert" if np.argmax(prediction) == 0 else "Extrovert"
        confidence = float(np.max(prediction))
        
        return {
            "personality": personality_type,
            "confidence": confidence,
            "status": "success"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Personality Prediction API",
        "docs": "/docs",
        "health": "OK"
    }

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}