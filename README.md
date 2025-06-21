# Personality Prediction API

A FastAPI-based REST API for predicting personality type (Introvert/Extrovert) based on behavioral features.

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



## Personality Prediction API

This API predicts personality type based on user input features using a trained machine learning model.

## Base URL

```
https://decryptogen-personality-api-f1f379d06e9a.herokuapp.com/
```

## Endpoints

### 1. Health Check
- **GET** `/health`
- **Description:** Check if the API is running.
- **Response:**
  ```json
  { "status": "healthy" }
  ```

### 2. Predict Personality
- **POST** `/predict`
- **Description:** Predicts the personality type from input features.
- **Request Body (JSON):**
  ```json
  {
    "Time_spent_Alone": 5.0,
    "Social_event_attendance": 2.0,
    "Going_outside": 3.0,
    "Friends_circle_size": 4.0,
    "Post_frequency": 1.0,
    "Stage_fear": "Yes",
    "Drained_after_socializing": "No"
  }
  ```
- **Response:**
  ```json
  {
    "predicted_personality": "Extrovert"
  }
  ```

## Example Usage (with curl)

```sh
curl -X POST \
  https://decryptogen-personality-api-f1f379d06e9a.herokuapp.com/predict \
  -H 'Content-Type: application/json' \
  -d '{
    "time_spent_alone": 20.0,
    "social_event_attendance": 0.0,
    "going_outside": 0.0,
    "friends_circle_size": 0.0,
    "post_frequency": 0.0,
    "stage_fear": true,
    "drained_after_socializing": true
  }'
```

## Notes
- All fields are required.
- Input values must match the expected types (numbers for numeric fields, true/false for boolean fields).

