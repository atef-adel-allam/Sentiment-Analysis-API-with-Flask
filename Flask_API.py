from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model (ensure path is correct)
model = load_model('sentiment_model.h5')

# Initialize the tokenizer
tokenizer = Tokenizer(num_words=5000)  # Adjust according to your training tokenizer
max_len = 200  # Adjust based on your training parameters

# Preprocess input text
def preprocess_text(text):
    sequences = tokenizer.texts_to_sequences([text])
    padded_text = pad_sequences(sequences, maxlen=max_len)
    return padded_text

# Get model prediction (sentiment)
def get_prediction(text):
    processed_text = preprocess_text(text)
    prediction = model.predict(processed_text)
    sentiment = "positive" if prediction >= 0.5 else "negative"
    return sentiment, float(prediction[0][0])  # Convert prediction to native float

# Endpoint to predict sentiment
@app.route('/predict', methods=['POST'])
def predict_sentiment():
    data = request.get_json()
    text = data['text']
    
    # Debug prints to show intermediate values
    print("Raw text:", text)
    processed_text = preprocess_text(text)
    print("Processed text:", processed_text)
    
    # Get model's prediction
    sentiment, score = get_prediction(text)
    print("Raw prediction score:", score)
    
    # Return the sentiment and prediction score as a JSON response
    return jsonify({"sentiment": sentiment, "prediction_score": score})

if __name__ == '__main__':
    app.run(debug=True)


# curl -X POST -H "Content-Type: application/json" -d '{"text": "I love this movie!"}' http://127.0.0.1:5000/predict 