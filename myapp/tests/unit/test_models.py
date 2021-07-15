# note file needs to be run from myapp/

# cd two levels up i.e. to myapp
# now the imported functions in app.py will work
import os
import sys
topdir = os.path.join(os.path.dirname(__file__), "../..")
sys.path.append(topdir)

import pytest
from unittest import mock
from myapp.models import predict_summariser, predict_sentiment, predict_subjectivity, flesch_reading_score, get_reduced_text_perc

# sample data
sample_input_text = """
    Nigeria pulled off one of the greatest upsets in international basketball history on Saturday night by stunning Team USA in an Olympic exhibition game in Las Vegas, beating them 90-87.

    It was Team USA's first-ever loss to an African nation. They had defeated Nigeria 156-73 in August 2012 at the London Olympics.

    Nigeria featured six NBA players and are coached by former NBA head coach and current Golden State Warriors assistant Mike Brown.
    """
sample_output_text = 'Nigeria pulled off one of the greatest upsets in international basketball history on Saturday night by stunning Team USA in an Olympic exhibition game in Las Vegas, beating them 90-87.'
dummy_reduced_text_perc = 'Text reduced by 58.9% (30 words/73)'


class TestExpectedInputOutput:
    def test_flesch_reading_score(self):
        assert flesch_reading_score(sample_input_text) == 'Readability score: 25.97'

    @mock.patch ("myapp.models.get_reduced_text_perc")
    def test_predict_summariser(self, mock_get_reduced_text_perc):
        mock_get_reduced_text_perc.return_value = dummy_reduced_text_perc
        assert predict_summariser(sample_input_text, 30) == (sample_output_text, dummy_reduced_text_perc)

    def test_predict_sentiment(self):
        assert predict_sentiment(sample_input_text) == 'Positive sentiment: +0.18'

    def test_predict_subjectivity(self):
        assert predict_subjectivity(sample_input_text) == 'Subjectivity score: 0.41'

    def test_get_reduced_text_perc(self):
        assert get_reduced_text_perc("hi there kids", "hi") == "Text reduced by 66.67% (1 words/3)"


class TestDataTypes:
    def test_output_type_flesch_reading_score(self):
        assert type(flesch_reading_score(sample_input_text)) == str

    @mock.patch("myapp.models.get_reduced_text_perc")
    def test_output_type_predict_summariser(self, mock_get_reduced_text_perc):
        mock_get_reduced_text_perc.return_value = dummy_reduced_text_perc
        assert type(predict_summariser(sample_input_text, 30)) == tuple

    def test_output_type_predict_sentiment(self):
        assert type(predict_sentiment(sample_input_text)) == str

    def test_output_type_predict_subjectivity(self):
        assert type(predict_subjectivity(sample_input_text)) == str


class TestExpectedErrors:
    def test_type_error_flesch_reading_score(self):
        with pytest.raises(TypeError):
            flesch_reading_score(3)

    def test_type_error_predict_summariser(self):
        with pytest.raises(TypeError):
            predict_summariser(3, 30)

    def test_type_error_predict_sentiment(self):
        with pytest.raises(TypeError):
            predict_sentiment(3)

    def test_type_error_predict_subjectivity(self):
        with pytest.raises(TypeError):
            predict_subjectivity(3)


