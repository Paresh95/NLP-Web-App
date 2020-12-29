from utils import get_reduced_text_perc, url_text_extractor
import textstat
from nrclex import NRCLex
from SimpleText.preprocessor import lowercase, strip_accents, strip_punctuation, strip_url 
from gensim.summarization.summarizer import summarize
import validators


def predict_summariser(summary_text, length):
    """
    Input
    ----------
    summary_text (string): Text to summarise or a URL to scrape the text from
    length (string): A integar value specifying the % of text to summarised

    Returns
    ----------
    Summarised text 
    """

    # get the % of text to be summarised
    ratio = int(length)/100

    # check if text input is a url, if so extract text else use text provided
    valid = validators.url(summary_text)

    if valid is True:
        summary_text = url_text_extractor(summary_text)
    else:
        pass
    
    summarised_text = summarize(summary_text, ratio=ratio, word_count=None, split=False)
    reduced_perc = get_reduced_text_perc(summary_text, summarised_text)

    return summarised_text, summary_text, reduced_perc


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