FROM python:3.8.2-slim-buster

RUN apt update
WORKDIR /app
ADD requirements.txt requirements.txt
RUN pip install -r /app/requirements.txt
ADD . /app

# Set application config
ENV DEBUG_MODE False

CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]