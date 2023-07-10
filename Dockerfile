FROM python:alpine

WORKDIR /

COPY . .

RUN pip install Flask

EXPOSE 5000

CMD ["python", "app.py"]