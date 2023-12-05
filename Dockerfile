FROM python:3.10
MAINTAINER Óscar García <oscar.gpoblacion@uah.es>

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY app /app
CMD python main.py 
