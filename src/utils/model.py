from flask import current_app
from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# def load_model():

#     # Load the IMDb dataset with a vocabulary limit of 50 words
#     (x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=30000)

#     # Get the word-to-index mapping
#     word_index = imdb.get_word_index()

#     return word_index
#     # Reverse the mapping to get index-to-word
#     index_to_word = {index: word for word, index in word_index.items()}

# Function to convert a review text to its integer sequence



def text_to_sequence(review_text, max_len=80):
    model = current_app.config['SENTIMENT_ANALYSIS_MODEL']

    word_index = imdb.get_word_index()

    # Tokenize the text using the IMDb dataset vocabulary
    tokenizer = Tokenizer(num_words=50, oov_token="<OOV>")
    tokenizer.word_index = {key: val for key, val in word_index.items() if val <= 30000}
    
    # Convert text to integer sequence
    sequence = tokenizer.texts_to_sequences([review_text])

        # Filter out None values in the sequence
    sequence = [index for index in sequence[0] if index is not None]


    new_review_padded = pad_sequences([sequence], maxlen=80)
    # padded_sequence = pad_sequences(sequence, maxlen=max_len, padding='post', truncating='post')

    return new_review_padded

def normalize_to_range(value, min_val, max_val, new_min, new_max):
    normalized_value = ((value - min_val) / (max_val - min_val)) * (new_max - new_min) + new_min
    return normalized_value
