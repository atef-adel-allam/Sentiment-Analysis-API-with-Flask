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
<<<<<<< HEAD
    return render_template('home.html')
=======
    return '''
    <html>
        <head>
            <title>Sentiment Analysis API</title>
            <style>
                body {
                    text-align: center;
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f9;
                }
                h1 {
                    color: #4CAF50;
                    animation: fadeIn 2s ease-in-out;
                }
                p {
                    color: #333;
                    font-size: 18px;
                }
                @keyframes fadeIn {
                    0% { opacity: 0; transform: translateY(-20px); }
                    100% { opacity: 1; transform: translateY(0); }
                }
            </style>
        </head>
        <body>
            <h1>Welcome to the Sentiment Analysis API!</h1>
            <p>Use the <strong>/predict</strong> endpoint to get predictions.</p>
        </body>
    </html>
    '''


>>>>>>> 4662351b3c45126f9f2d28fa55ccaade12c10260
@app.route('/predict', methods=['POST'])
def predict():
    
    input_text = request.json['text']

    # Transform the input text to TF-IDF features
    input_tfidf = tfidf_vectorizer.transform([input_text])

    prediction = model.predict(input_tfidf)
    
    prediction_prob = model.predict_proba(input_tfidf)[0]

    # Interpret the prediction: 1 is positive, 0 is negative
    if prediction[0] == 1:
        sentiment = "Positive"
        score = prediction_prob[1]  
    else:
        sentiment = "Negative"
        score = prediction_prob[0] 

    # Return the sentiment and score as JSON response
    return jsonify({
        'sentiment': sentiment,
        'score': round(score, 4)
    })

if __name__ == '__main__':
    app.run(debug=True)
