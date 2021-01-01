from flask import Flask, request, render_template
from models import predict_summariser, predict_sentiment, predict_subjectivity, flesch_reading_score
from newspaper.article import ArticleException
from utils import check_for_url


app = Flask(__name__)

### Default pages before input text ###

@app.route('/')
def home():
    return render_template("homepage.html") 


@app.route('/summariser')
def summariser():
    return render_template("summariser.html", default_slider_value=40) 


@app.route('/sentiment')
def sentiment():
    return render_template("sentiment.html")


@app.route('/miscellaneous')
def miscellaneous():
    return render_template("miscellaneous.html")


### Pages after text input ###

@app.route("/summariser", methods=['POST'])
def summariser2():
    summary_text = """{}""".format(request.form['input-summary-text'])
    slider_value = request.form["slider-value"]

    summary_text = check_for_url(summary_text)
    summarised_text, reduced_perc = predict_summariser(summary_text, length=slider_value)

    return render_template('summariser.html', summarised_text=summarised_text, \
        summary_text=summary_text, reduced_text_perc=reduced_perc, \
            default_slider_value=slider_value)


@app.route("/sentiment", methods=['POST'])
def sentiment2():
    input_text = """{}""".format(request.form['input-sentiment-text'])
    input_text = check_for_url(input_text) # check if text or url and web scrap if url
    
    sentiment = predict_sentiment(input_text)
    interpretation = "*Interpretation - Sentiment ranges from 1 (extremely positive) to -1 \
        (extremely negative)."

    return render_template('sentiment.html', input_text=input_text, sentiment=sentiment, interpretation=interpretation)


@app.route("/miscellaneous", methods=['POST'])
def miscellaneous2():
    input_text = """{}""".format(request.form['input-miscellaneous-text'])

    input_text = check_for_url(input_text)

    subjectivity = predict_subjectivity(input_text)
    readability = flesch_reading_score(input_text)

    interpretation = "*Interpretation - Subjectivity ranges from 1 (very subjective) to \
            0 (very objective). Readability ranges from 100 (very easy to read) to 0 (very difficult to read)."

    return render_template('miscellaneous.html', input_text=input_text, \
        subjectivity=subjectivity, readability=readability, interpretation=interpretation)


### Error handling ### 

@app.errorhandler(Exception)
def server_error(err):
    """
    Catches generic error and returns general error HTML page
    """
    app.logger.exception(err)
    return render_template('generalError.html'), 500

 
@app.errorhandler(IndexError)
def index_error(err):
    """
    Catches index error and returns index error HTML page
    """
    app.logger.exception(err)
    return render_template('indexError.html'), 500


@app.errorhandler(ArticleException)
def input_url_error(err):
    """
    Catches input url error and returns incorrect url error HTML page
    """
    app.logger.exception(err)
    return render_template('incorrectUrlError.html'), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
