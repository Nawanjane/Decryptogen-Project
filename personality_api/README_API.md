# Personality Prediction API

This API allows you to predict personality traits using a trained machine learning model via FastAPI. The app is deployed on Heroku and can be accessed publicly.

## Base URL

```
https://decryptogen-personality-api-f1f379d06e9a.herokuapp.com/
```

---

## Endpoints

### 1. Health Check

**GET** `/health`

- Returns: `{ "status": "ok" }`
- Use this to verify the API is running.

#### Example
```
curl https://decryptogen-personality-api-f1f379d06e9a.herokuapp.com/health
```

---

### 2. Predict Personality

**POST** `/predict`

- Accepts: JSON body with the required features for prediction.
- Returns: Predicted personality type or probabilities.

#### Example Request
```
curl -X POST \
  https://decryptogen-personality-api-f1f379d06e9a.herokuapp.com/predict \
  -H 'Content-Type: application/json' \
  -d '{
    "feature1": value1,
    "feature2": value2,
    ...
  }'
```

#### Example Response
```
{
  "prediction": "INTJ"
}
```

---

## Input Format
- The input JSON keys and values must match the features expected by the model.
- Refer to your model's training features for the exact input schema.

---

## Error Handling
- The API returns standard HTTP error codes and messages for invalid input or server errors.

---

## Deployment Notes
- The app is deployed on Heroku free tier. There may be a short delay on the first request if the app is sleeping.

---

## Contact
For questions or issues, please open an issue on the GitHub repository or contact the maintainer.
