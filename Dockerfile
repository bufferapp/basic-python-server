FROM python:3.7

RUN pip install flask
COPY app.py /src/app.py
WORKDIR /src

ENV FLASK_APP=app.py
ENV PYTHONUNBUFFERED=nonempty
EXPOSE 5000
CMD flask run -h 0.0.0.0
