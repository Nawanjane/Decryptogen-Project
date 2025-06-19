import tensorflow as tf

# Load the model using TensorFlow's Keras
model = tf.keras.models.load_model('Decryptogen-Project/personality_api/modles/best_model.h5')

# Save the model again using the same TensorFlow version as on Heroku
model.save('Decryptogen-Project/personality_api/modles/best_model_heroku.h5')
