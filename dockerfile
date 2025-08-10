
FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDOWNWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 1000

CMD [ "sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:1000" ]
