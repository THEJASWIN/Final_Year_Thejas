FROM python:3.9-slim

COPY ./requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD exec gunicorn --bind :8000 --workers 3 --worker-class uvicorn.workers.UvicornWorker  --threads 8 --timeout 3600 api:app