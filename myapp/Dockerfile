FROM python:3.6.12
WORKDIR /myapp
ADD . /myapp
RUN pip3 -q install pip --upgrade
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]