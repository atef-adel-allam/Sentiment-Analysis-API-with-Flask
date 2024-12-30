# Sentiment-Analysis-API-with-Flask

This repository provides a complete solution for sentiment analysis using **Flask-based APIs**, **pre-trained models** (Logistic Regression and Deep Learning), and tools like a **TF-IDF vectorizer**. The project is designed to efficiently classify text sentiment, offering a seamless way to integrate sentiment analysis into web applications.

---

## **Dataset**

The **IMDb dataset** is used as the foundation for training and testing the sentiment analysis models. This dataset contains 50,000 labeled movie reviews, preprocessed for feature extraction and modeling.

You can download the dataset from the following link:
[Stanford AI IMDb Dataset](https://ai.stanford.edu/~amaas/data/sentiment/)

---

## **Project Overview**

This project leverages Flask APIs to provide real-time sentiment predictions. It uses a combination of **Logistic Regression**, **Deep Learning models**, and **TF-IDF vectorization** to classify text as either "Positive" or "Negative." The solution is built

for seamless integration into modern applications like customer feedback analysis and social media monitoring.

### **Key Components**
1. **Flask API**:
   - A REST API to handle incoming requests and return sentiment predictions.
2. **Machine Learning Models**:
   - Pre-trained Logistic Regression and Deep Learning models.
   - TF-IDF vectorizer for feature extraction.
3. **Dockerized Deployment**:
   - Containerized the API for portability and scalability.
4. **Jupyter Notebook**:
   - Includes training and experimentation workflows.

---

## **Features**
- **Pre-trained Models**: Includes Logistic Regression and Deep Learning.
- **Easy Integration**: RESTful API for seamless web application integration.
- **Tools**: TF-IDF vectorizer and IMDb dataset for preprocessing.
- **Dockerized Deployment**: Ensures scalability and portability.
- **API Endpoints**:
  - `/predict` - Accepts JSON input to analyze sentiment.
  - `/` - Displays a welcome page with project information.

---

## **How to Use**

### **1. Clone the Repository**
```bash
git clone https://github.com/atef-adel-allam/Sentiment-Analysis-API-with-Flask.git
cd Sentiment-Analysis-API-with-Flask
```

### **2. Build the Docker Image**
```bash
docker build -t sentiment-analysis-api .
```

### **3. Run the Flask API**
```bash
docker run -d -p 5000:5000 sentiment-analysis-api
```

### **4. Access the API**
- Open a browser and navigate to `http://localhost:5000/` to view the welcome page.
- Use the `/predict` endpoint to send JSON input and get sentiment predictions.

Example:
```json
POST /predict
{
    "text": "This movie was amazing!"
}
```

---

## **Applications**
- **Customer Feedback Analysis**:
   - Analyze customer reviews to determine satisfaction levels.
- **Social Media Monitoring**:
   - Classify sentiment in tweets, posts, or comments.
- **Content Moderation**:
   - Filter negative content in forums or platforms.

---

## **Contact**
For questions or support, feel free to reach out:

**Atef Adel**  
📞 +201111449824  
✉️ atef.i.allam@gmail.com  
