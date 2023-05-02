from textblob import TextBlob



def textblob_sentiment(self, text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment < 0:
        label = 'neg'
    elif sentiment == 0:
        label = 'neu'
    elif sentiment > 0:
        label = 'pos'
    return label 
