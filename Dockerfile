FROM python:3.10.10

RUN mkdir /app
WORKDIR "/app"

RUN pip install --upgrade pip

ADD requirements.txt /app/
RUN pip install -r /app/requirements.txt

RUN mkdir /app/data
ADD data/lastfm_artist_list.csv /app/data/
ADD data/lastfm_user_scrobbles.csv /app/data/

RUN mkdir /app/research
ADD research/als.pkl /app/research/

ADD main.py /app/
ADD menu.py /app/
ADD solution.py /app/