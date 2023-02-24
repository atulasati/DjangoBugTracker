FROM python:3.11.2-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY . .


EXPOSE 8000

CMD ["python", "manage.py", "runserver"]
