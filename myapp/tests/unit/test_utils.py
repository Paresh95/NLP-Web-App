# note file needs to be run from myapp/

# cd two levels up i.e. to myapp
# now the imported functions in app.py will work
import os
import sys
topdir = os.path.join(os.path.dirname(__file__), "../..")
sys.path.append(topdir)

from myapp.utils import url_text_extractor, check_for_url
from unittest import mock

# sample data
url = "https://finance.yahoo.com/news/apple-aapl-stock-sinks-market-214509540.html?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAH3WVLNFE9hGT29Bpina0F7MsJrj5TVtIVvjAeniqDcQSfDNjlgHSsNF1PaTnZkjw6irflerPLx-GCwRSATusxGRSpIfmkmsrb8I1BJTBF4rfO_dGYJ4d3eYxFZB6MaPBoiQOQK4RTJ_Mki4lxdTbXDw9q-nYl4qwGG-kFw6-REW"
article_first_50_characters = 'Apple (AAPL) closed the most recent trading day at'
clean_article_last_50_characters = 'n Zacks.com click here. Zacks Investment Research'
text = "I went to the shops \n\n\n\npeople love it."
clean_text = 'I went to the shops   people love it.'


def test_url_text_extractor_first_50_characters():
    assert url_text_extractor(url)[:50] == article_first_50_characters


@mock.patch("myapp.utils.url_text_extractor")
def test_check_url_with_url(mock_url_text_extractor):
    mock_url_text_extractor.return_value = clean_article_last_50_characters
    assert check_for_url(url) == clean_article_last_50_characters
    mock_url_text_extractor.assert_called_once()


def test_check_url_with_text():
    assert check_for_url(text) == clean_text

