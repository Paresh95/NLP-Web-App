# NLP-Web-App

**Note: Unfortunately, Heroku has removed their free tier so this web app is no longer deployed.**

A flask web app to showcase some simple Natural Language Processing (NLP) techniques to analyse text. The web app is deployed via Heroku (note heroku has depreciated it's free tier as of the 28th November 2022 and hence this app is not currently deployed).

### Website link: https://nlp-with-paresh.herokuapp.com/ 

Note: it may takes 30 seconds to start up if unused in the last 30 minutes. I am pinging the server every 30 mins to stop this happening, but Heroku requires I shut the app down for 6 hours a day - I've chosen 2am-8am UK time. 

<br>
*Example screenshots of the Web Application:*

<p align="center">
<img src=website_progress_images/Version%200.91.png width=100%>
<img src=website_progress_images/Version%200.93.png width=100%>
<img src=website_progress_images/Version%200.95.png width=100%>
<img src=website_progress_images/Version%200.96.png width=100%>
</p>


### How to run locally with Docker

1) `cd` into the `NLP-Web-App/myapp` folder on your terminal. 

2) Install [Docker](https://docs.docker.com/get-docker/)

3) On your terminal run `docker build -t nlp-web-app .`. This tells Docker to build a container called 'nlp-web-app' from the set of instructions in the Dockerfile which resides in the current working directory. 

4) Next run `docker run -p 5000:5000 nlp-web-app`. This runs your container on your local server and forwards the request from port 5000 on the host (your computer) to port 5000 in the container. 

5) Access the web app via `http://0.0.0.0:5000/`

### Google analytics
https://m.youtube.com/watch?v=f3X-hYRxBL8

### Heroku Kaffeine

http://kaffeine.herokuapp.com/#!

### Heroku documentation.
https://devcenter.heroku.com/articles/getting-started-with-python#deploy-the-app

`heroku ps:scale web=1`

`heroku apps:rename nlp-with-paresh`

`heroku ps -a nlp-with-paresh` --> Checks usage
