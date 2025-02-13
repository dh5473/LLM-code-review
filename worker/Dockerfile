FROM python:3.12

WORKDIR /worker

COPY ./requirements.txt /worker/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /worker/requirements.txt

COPY . /worker

ENTRYPOINT celery -A tasks worker --loglevel=info
#CMD ["celery", "-A", "tasks", "worker", "--loglevel=info"]
