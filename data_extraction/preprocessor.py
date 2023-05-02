import re
import emoji
import nltk
nltk.download()

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def preprocess_tweet(tweet):
    """
    Preprocesses a tweet for sentiment analysis by performing the following steps:
    1. Removing URLs and mentions
    2. Converting emojis to their descriptions
    3. Removing punctuation and converting to lowercase
    4. Tokenizing the tweet into words
    5. Removing stop words
    6. Lemmatizing words
    
    Args:
    tweet (str): The tweet to preprocess
    
    Returns:
    preprocessed_tweet (str): The preprocessed tweet
    """
    # Remove URLs and mentions
    tweet = re.sub(r"http\S+|www\S+|https\S+|@\S+", "", tweet)
    
    # Convert emojis to their descriptions
    tweet = emoji.demojize(tweet)
    tweet = re.sub(r":\S+:", lambda m: " ".join(m.group(0).replace(":", "").replace("_", " ").split()), tweet)
    
    # Remove punctuation and convert to lowercase
    tweet = re.sub(r"[^\w\s]", "", tweet)
    tweet = tweet.lower()
    
    # Tokenize the tweet into words
    words = word_tokenize(tweet)
    
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if not word in stop_words]
    
    # Lemmatize words
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    
    # Join the words back into a string
    preprocessed_tweet = " ".join(words)
    
    return preprocessed_tweet