FROM python:alpine

WORKDIR /

COPY . .

RUN pip install Flask

CMD ["python", "app.py"]