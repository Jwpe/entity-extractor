FROM trackmaven/nltk
MAINTAINER Jonathan Evans "jon@trackmaven.com"

RUN pip install requests beautifulsoup4 numpy flask flask_nicely

ADD app /app

WORKDIR /app

EXPOSE 5000 5000

CMD ["python app.py"]