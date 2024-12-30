from flask import Flask, request, jsonify, render_template
import pickle


# Initialize Flask app
app = Flask(__name__)

# Load the saved model and vectorizer
with open('logistic_regression_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
    tfidf_vectorizer = pickle.load(vectorizer_file)



@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return render_template('predict.html')
    
    if request.method == 'POST':
        input_text = request.json.get('text')

        # Transform the input text to TF-IDF features
        input_tfidf = tfidf_vectorizer.transform([input_text])
        prediction = model.predict(input_tfidf)
        prediction_prob = model.predict_proba(input_tfidf)[0]

        # Interpret the prediction: 1 is positive, 0 is negative
        sentiment = "Positive" if prediction[0] == 1 else "Negative"
        score = prediction_prob[1] if prediction[0] == 1 else prediction_prob[0]

        # Return the sentiment and score as JSON response
        return jsonify({
            'sentiment': sentiment,
            'score': round(score, 4)
        })


if __name__ == '__main__':
    app.run(debug=True)
