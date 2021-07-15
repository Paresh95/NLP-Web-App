from utils import get_reduced_text_perc
from gensim.summarization.summarizer import summarize
import textstat
from textblob import TextBlob


def predict_summariser(summary_text, length):
    """
    Input
    ----------
    summary_text (string): Text to summarise 
    length (string): A integar value specifying the % of text to summarised

    Returns
    ----------
    Summarised text 
    """

    ratio = int(length)/100 # gets the % of text to be summarised
    summarised_text = summarize(summary_text, ratio=ratio, word_count=None, split=False)
    reduced_perc = get_reduced_text_perc(summary_text, summarised_text)

    return summarised_text, reduced_perc


def predict_sentiment(text):
    """
    Input
    ----------
    text(string)

    Returns
    ----------
    The sentiment and sentiment score ranging from [-1,1] (integar)
    """

    TextBlob_object = TextBlob(text)
    sentiment_score = round(TextBlob_object.sentiment.polarity, 2)
    
    if sentiment_score == 0:
        output = "Neutral sentiment: " + str(sentiment_score)
    elif sentiment_score > 0:
        output = "Positive sentiment: +" + str(sentiment_score)
    else:
        output = "Negative sentiment: " + str(sentiment_score)
   
    return output 


def predict_subjectivity(text):
    """
    Input
    ----------
    text(string)

    Returns
    ----------
    The subjectivity score ranging from [0,1] (integar)
    """

    TextBlob_object = TextBlob(text)
    subjectivity_score = round(TextBlob_object.sentiment.subjectivity, 2)
    output = "Subjectivity score: " + str(subjectivity_score)
    
    return output


def flesch_reading_score(text):
    """
    Input
    ----------
    text(string)

    Returns
    ----------
    The Flesch Reading Ease score ranging from [0,100] (integar)
    """
    
    # note this has to be completed before text preprocessing
    readability_score = round(textstat.flesch_reading_ease(text), 2)

    output = "Readability score: " + str(readability_score)

    return output


