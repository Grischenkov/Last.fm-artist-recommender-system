FROM python:3.10.10

RUN mkdir /app
WORKDIR "/app"

RUN pip install --upgrade pip

ADD requirements.txt /app/
RUN pip install -r /app/requirements.txt

ADD data /app/data

ADD main.py /app/
ADD menu.py /app/
ADD solution.py /app/