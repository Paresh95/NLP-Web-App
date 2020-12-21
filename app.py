from flask import Flask, request, render_template
from models import predict_summariser
from utils import get_reduced_text_perc


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("homepage.html") 

@app.route('/summariser')
def summariser():
    return render_template("summariser.html") 


@app.route("/summariser", methods=['POST'])
def home2():
    summary_text = """{}""".format(request.form['summary text'])
    # if user forgets to input values for min/max words they default to 20 and 1000
    try:
        min_words = int(request.form['min words'])
    except:
        min_words = 20

    try:
         max_words = int(request.form['max words'])
    except:
        max_words = 650

    summarised_text = predict_summariser(summary_text, min_words=min_words, max_words=max_words)
    reduced_text_perc = get_reduced_text_perc(summary_text=summary_text, summarised_text=summarised_text )

    return render_template('summariser.html', summarised_text=summarised_text, \
        summary_text=summary_text, min_words=min_words, max_words=max_words, reduced_text_perc=reduced_text_perc)



@app.errorhandler(Exception)
def server_error(err):
    app.logger.exception(err)
    return render_template('generalError.html'), 500
 
@app.errorhandler(IndexError)
def server_error(err):
    app.logger.exception(err)
    return render_template('indexError.html'), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)







from time import time 

s = time()

#print(predict_summariser(ARTICLE, min_words=90, max_words=150))
#print(predict_sentiment(ARTICLE))
#print(flesch_reading_score(ARTICLE))
#print(get_emotion_scores(ARTICLE))
e = time()
print(e-s)