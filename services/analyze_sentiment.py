from transformers import pipeline

class AnalyzingSentimentService:
    
 @staticmethod
 def analyze_sentiment(text):
    sentiment_pipeline = pipeline("sentiment-analysis")
    result = sentiment_pipeline(text)
    sentiment = result[0]['label']
    return sentiment
