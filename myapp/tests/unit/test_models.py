import sys
import os
import pytest

# get current working directory
cwd = os.getcwd()

# change the sys path - allows modules from other folders to be imported
sys.path.append(cwd)

from myapp.models import predict_summariser, predict_sentiment, predict_subjectivity, flesch_reading_score


sample_text = """
    Nigeria pulled off one of the greatest upsets in international basketball history on Saturday night by stunning Team USA in an Olympic exhibition game in Las Vegas, beating them 90-87.

    It was Team USA's first-ever loss to an African nation. They had defeated Nigeria 156-73 in August 2012 at the London Olympics.

    Nigeria featured six NBA players and are coached by former NBA head coach and current Golden State Warriors assistant Mike Brown.
    """


class TestExpectedInputOutput:
    def test_flesch_reading_score(self):
        assert flesch_reading_score(sample_text) == 'Readability score: 25.97'

    def test_predict_summariser(self):
        assert predict_summariser(sample_text, 30) == ('Nigeria pulled off one of the greatest upsets in international basketball history on Saturday night by stunning Team USA in an Olympic exhibition game in Las Vegas, beating them 90-87.', 'Text reduced by 58.9% (30 words/73)')

    def test_predict_sentiment(self):
        assert predict_sentiment(sample_text) == 'Positive sentiment: +0.18'

    def test_predict_subjectivity(self):
        assert predict_subjectivity(sample_text) == 'Subjectivity score: 0.41'


class TestDataTypes:
    def test_output_type_flesch_reading_score(self):
        assert type(flesch_reading_score(sample_text)) == str

    def test_output_type_predict_summariser(self):
        assert type(predict_summariser(sample_text, 30)) == tuple

    def test_output_type_predict_sentiment(self):
        assert type(predict_sentiment(sample_text)) == str

    def test_output_type_predict_subjectivity(self):
        assert type(predict_subjectivity(sample_text)) == str


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


