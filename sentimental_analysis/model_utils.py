from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer



class SentimentAnalyzer:
    
    def __init__(self):
        self.vader_model = SentimentIntensityAnalyzer()
       
    def vader_sentiment(self, text):
        sentiment = self.vader_model.polarity_scores(text)
        # Remove the 'compound' key from the dictionary
        del sentiment['compound']
        # Get the key with the maximum value
        label = max(sentiment, key=sentiment.get)
        return label


