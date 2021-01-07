FROM python:3.6.12
WORKDIR /project
ADD . /project
RUN pip3 -q install pip --upgrade
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["gunicorn", "run", "-h", "0.0.0.0", "-p", "5000"]