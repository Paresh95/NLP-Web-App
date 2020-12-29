from flask import Flask, request, render_template
from models import flesch_reading_score, get_emotion_scores, predict_summariser #, predict_sentiment
from newspaper.article import ArticleException


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("homepage.html") 

@app.route('/summariser')
def summariser():
    return render_template("summariser.html", default_slider_value=40) 


@app.route("/summariser", methods=['POST'])
def home2():
    summary_text = """{}""".format(request.form['summary text'])
    slider_value = request.form["slider-value"]

    summarised_text, summary_text, reduced_perc = predict_summariser(summary_text, length=slider_value)

    return render_template('summariser.html', summarised_text=summarised_text, \
        summary_text=summary_text, reduced_text_perc=reduced_perc, default_slider_value=slider_value)


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
