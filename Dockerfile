FROM python:3.9-slim-buster

WORKDIR /app

copy requirements.txt .

RUN pip3 install --upgrade pip && pip3 install -r ./requirements.txt --no-cache-dir

COPY . .

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]