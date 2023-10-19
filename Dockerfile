FROM python:3.11
LABEL authors="mikitomi21"

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

CMD ["python", "main.py"]