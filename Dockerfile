FROM python:alpine

WORKDIR /

COPY . .

RUN pip install Flask
RUN pip install psycopg2-binary

EXPOSE 5000

CMD ["python", "app.py"]