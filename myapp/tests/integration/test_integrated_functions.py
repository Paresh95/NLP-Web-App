# note file needs to be run from myapp/

# cd two levels up i.e. to myapp
# now the imported functions in app.py will work
import os
import sys
topdir = os.path.join(os.path.dirname(__file__), "../..")
sys.path.append(topdir)

import pytest
from myapp.models import predict_summariser


# sample data
test_data_paragraph = """
In Wales, masks are still legally required in all public indoor areas, apart from when seated to eat or drink. 
If there is a move to alert level zero on 7 August, masks will still be required in most public places and on public 
transport.
In Northern Ireland from 26 July (if plans are approved on 22 July) face coverings will no longer be compulsory in places of worship, or for students in school classrooms. 
They must still be worn on public transport and in shops and hospitality venues.
"""

test_data_nonfunctional_url = "https://www.bbc.co.uk/news/health-512"

sample_input_text = """
    Nigeria pulled off one of the greatest upsets in international basketball history on Saturday night by stunning Team USA in an Olympic exhibition game in Las Vegas, beating them 90-87.

    It was Team USA's first-ever loss to an African nation. They had defeated Nigeria 156-73 in August 2012 at the London Olympics.

    Nigeria featured six NBA players and are coached by former NBA head coach and current Golden State Warriors assistant Mike Brown.
    """
sample_output_text = 'Nigeria pulled off one of the greatest upsets in international basketball history on Saturday night by stunning Team USA in an Olympic exhibition game in Las Vegas, beating them 90-87.'
dummy_reduced_text_perc = 'Text reduced by 58.9% (30 words/73)'


@pytest.mark.parametrize("route, input_form_text, test_data, status_code",
                         [("/sentiment", 'input-sentiment-text', test_data_paragraph, 200),
                          ("/subjectivity", 'input-subjectivity-text', test_data_paragraph,  200),
                          ("/readability", 'input-readability-text', test_data_paragraph, 200),
                          ("/sentiment", 'input-sentiment-text', test_data_nonfunctional_url, 500),
                          ("/subjectivity", 'input-subjectivity-text', test_data_nonfunctional_url,  500),
                          ("/readability", 'input-readability-text', test_data_nonfunctional_url, 500)
                          ])
def test_web_page_simple_post(client, route, input_form_text, test_data, status_code):
    sent = {
        input_form_text: test_data,
            }
    res = client.post(route, data=sent)
    assert res.status_code == status_code


@pytest.mark.parametrize("test_data, status_code",
                         [(test_data_paragraph, 200),
                          (test_data_nonfunctional_url, 500)
                          ])
def test_web_page_summariser_post(client, test_data, status_code):
    sent = {
        'input-summary-text': test_data,
        'slider-value': '40'
            }
    res = client.post("/summariser", data=sent)
    assert res.status_code == status_code


def test_predict_summariser():
    assert predict_summariser(sample_input_text, 30) == (sample_output_text, dummy_reduced_text_perc)