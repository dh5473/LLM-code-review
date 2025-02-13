FROM python:3.12

WORKDIR /backend

COPY ./requirements.txt /backend/requirements.txt
COPY ./src/.env .env

RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt

COPY ./src /backend/src

ENV PYTHONPATH="/backend"

WORKDIR /backend/src

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

