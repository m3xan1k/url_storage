FROM python:3.8-slim
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD uvicorn api.main:app --host 0.0.0.0 --port 8000
