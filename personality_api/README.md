# Personality Prediction API

A FastAPI-based REST API for predicting personality type (Introvert/Extrovert) based on behavioral features.

## Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd personality_api
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the API

```bash
uvicorn main:app --reload
```

The API will be available at http://localhost:8000

## API Endpoints

### POST /predict
Predicts personality type based on input features.

Example request:
```json
{
    "time_spent_alone": 7.5,
    "social_event_attendance": 2.0,
    "going_outside": 3.0,
    "friends_circle_size": 5.0,
    "post_frequency": 2.0,
    "stage_fear": true,
    "drained_after_socializing": true
}
```

Example response:
```json
{
    "personality": "Introvert",
    "confidence": 0.89,
    "status": "success"
}
```

### GET /health
Health check endpoint.

## Documentation
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
