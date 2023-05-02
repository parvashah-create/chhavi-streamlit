from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer



vader_model = SentimentIntensityAnalyzer()

def vader_sentiment(text):
        sentiment = vader_model.polarity_scores(text)
        # Remove the 'compound' key from the dictionary
        del sentiment['compound']
        # Get the key with the maximum value
        label = max(sentiment, key=sentiment.get)
        return label

