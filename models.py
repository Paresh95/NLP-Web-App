from transformers import pipeline


def predict_summariser(text, min_words=20, max_words=650):
    """
    Input
    ----------
    text (string)
    min_words (int): The minimum number of words to use for the summary
    max_words (int): The maximum number of words to use for the summary
    
    
    Returns
    ----------
    Summarised text
    """

    # if max_words exceeds words in text make the max_words = no. of words in the text
    if max_words > len(text.split()):
        max_words = len(text.split())

    # Note that "bart-large-cnn" is the default model for the summarization pipeline
    summarizer = pipeline("summarization")
    summarised_sentances = summarizer(text, min_length=min_words, max_length=max_words, do_sample=False, early_stopping=False)[0]['summary_text']
    
    # The above can output incomplete sentances, the below removes uncomplete sentances e.g. "I like. Hi" becomes "I like.""
    return summarised_sentances[ :summarised_sentances.rindex(".") + 1]
    
