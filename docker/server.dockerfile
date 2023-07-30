FROM python:3.11-slim-buster

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000
CMD ["python", "main.py"]
