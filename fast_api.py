from data_pipeline import pipeline
from database_utils.db_utils import DbUtils
from prompt.openai_utils import create_prompt, generate_response, generative_search

db_utils = DbUtils("tweet.db")



def brand_image_report(username, openai_key):
    new_tweets = pipeline(username)
    if new_tweets:
        tweets  = db_utils.get_recent_sentiments("tweets",username)
        prompt  = create_prompt(tweets)
        response  = generate_response(prompt,openai_key)
    else:
        response = "Pipeline error!"    
    return {"response":response}


def vector_search(string_input,openai_key):
    response = generative_search(string_input,openai_key)
    return {"response":response}
