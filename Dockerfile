FROM trackmaven/nltk
MAINTAINER Jonathan Evans "jon@trackmaven.com"

RUN pip install requests beautifulsoup4 numpy flask flask_nicely

RUN git clone git@github.com:Jwpe/entity-extractor.git /extractor

WORKDIR /extractor

CMD ["python"]