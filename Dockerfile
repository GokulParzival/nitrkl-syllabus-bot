FROM python:3.7-alpine

COPY app/app
COPY server.sh/app/server.sh

USER root

RUN pip install --upgrade pip
RUN pip install rasa-x==0.32.2 --extra-index-url https://pypi.rasa.com/simple
RUN pip install spacy
RUN pip install ujson
RUN python -m spacy download en
RUN python -m spacy download en_core_web_md
RUN python -m spacy link en_core_web_md en
RUN rasa train
RUN chmod a+rwx /app/server.sh

ENTRYPOINT ["/app/server.sh"]