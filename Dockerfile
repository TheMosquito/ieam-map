FROM python:3-alpine3.12

RUN pip3 install Flask
RUN pip3 install requests

WORKDIR /
COPY site.html /
COPY site.css /
COPY favicon.ico /
COPY logo.png /
COPY ./ieam-map.py /

CMD python3 ieam-map.py


