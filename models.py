#from transformers import pipeline
import textstat
from nrclex import NRCLex
from SimpleText.preprocessor import lowercase, strip_accents, strip_punctuation, strip_url 


# def predict_summariser(text, min_words=20, max_words=650):
# """
# Input
# ----------
# text (string)
# min_words (int): The minimum number of words to use for the summary
# max_words (int): The maximum number of words to use for the summary


# Returns
# ----------
# Summarised text
# """

# # if max_words exceeds words in text make the max_words = no. of words in the text
# if max_words > len(text.split()):
#     max_words = len(text.split())

# # Note that "bart-large-cnn" is the default model for the summarization pipeline
# summarizer = pipeline("summarization")
# summarised_sentances = summarizer(text, min_length=min_words, max_length=max_words, do_sample=False, early_stopping=False)[0]['summary_text']

# # The above can output incomplete sentances, the below removes uncomplete sentances e.g. "I like. Hi" becomes "I like.""
# return summarised_sentances[ :summarised_sentances.rindex(".") + 1]
    

# def predict_sentiment(text):
#     """
#     Input
#     ----------
#     text(string)

#     Returns
#     ----------
#     JSON object of sentiment (label) and sentiment score (score)
#     """

#     sentiment = pipeline('sentiment-analysis')
#     return sentiment(text)[0]


def flesch_reading_score(text):
    """
    Input
    ----------
    text(string)

    Returns
    ----------
    A Flesch Reading Ease score (integar)
    """
    # note this has to be completed before text preprocessing
    return textstat.flesch_reading_ease(text)


def get_emotion_scores(text):

    """
    Input
    ----------
    text(string)

    Returns
    ----------
    emotions_dictionary (list): Two items in the list: 1)  a dictionary of scores 
                                for each emotions and 2) a dictionary of emotions
                                and words from the text associated with the emotion
    """

    # preprocess the text 
    text = lowercase(text) 
    text = strip_accents(text)
    text = strip_punctuation(text)
    text = strip_url(text) 

    # instantiate the text object 
    text_object = NRCLex(text)

    # get scores for: fear, anger, trust, surprise, sadness, disgust, joy, anticipation 
    emotion_scores_dictionary = text_object.affect_frequencies
    keys = ['fear', 'anger', 'trust', 'surprise', 'sadness', 'disgust', 'joy', 'anticipation']
    filtered_emotion_scores_dictionary = dict((k, round(emotion_scores_dictionary[k], 4)) for k in keys if k in emotion_scores_dictionary)

    # get a dictionary of the words corresponding to each emotion
    words_emotions_dictionary = text_object.affect_dict

    # inverse the keys and values in the dictionary so the keys are emotions and values are the words
    emotions_words_dictionary = {}
    for k,v in words_emotions_dictionary.items():
        for x in v:
            emotions_words_dictionary.setdefault(x,[]).append(k)

    # get emotion/word association for: fear, anger, trust, surprise, sadness, disgust, joy, anticipation
    filtered_emotions_words_dictionary = dict((k, emotions_words_dictionary[k]) for k in keys if k in emotions_words_dictionary)

    emotions_output = [filtered_emotion_scores_dictionary, filtered_emotions_words_dictionary]

    return emotions_output