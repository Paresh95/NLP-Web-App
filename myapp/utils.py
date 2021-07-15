from newspaper import Article
import validators


def url_text_extractor(url):
    """
    Input
    ----------
    url (string)

    Returns
    ----------
    An article's text
    """
    article = Article(url)
    article.download()
    article.parse()

    return article.text


def check_for_url(text):
    """
    Check if text input is a url. If so it extracts the website text
    else it uses the input text.

    Input
    ----------
    text (string): Text or a url. 

    Returns
    ----------
    An article's text

    """
    
    valid = validators.url(text)

    if valid is True:
        text = url_text_extractor(text)
    else:
        pass

    # clean the text
    text = text.replace('\n', ' ').replace('\r', '').replace('  ', ' ')

    return text
