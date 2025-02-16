FROM ghcr.io/abetlen/llama-cpp-python:v0.3.5@sha256:632f1037e897bd53970f9ad11d886625f0c90e362e92b244fbbbaa816b2aafa6

WORKDIR /worker

COPY ./requirements.txt /worker/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /worker/requirements.txt

COPY . /worker

ENTRYPOINT celery -A tasks worker --loglevel=info
##CMD ["celery", "-A", "tasks", "worker", "--loglevel=info"]
