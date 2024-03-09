from flask import request,current_app
from utils.model import text_to_sequence , normalize_to_range


def set_sentiment_analysis_model(model):
    current_app.config['SENTIMENT_ANALYSIS_MODEL'] = model

def sentiment_analysis():
    model = current_app.config['SENTIMENT_ANALYSIS_MODEL']

    request_data=request.get_json(force=True)
    new_review=request_data["new_review"]
    user_review_sequence =text_to_sequence(new_review)
 
    predicted_sentiment = model.predict(user_review_sequence)
    min_value = 0
    max_value = 1
    new_min = 0
    new_max = 5

    normalized_value = normalize_to_range(predicted_sentiment[0][0], min_value, max_value, new_min, new_max)
    return str(normalized_value)