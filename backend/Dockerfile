FROM python:3.9-slim
RUN pip install flask requests prometheus-flask-exporter pymongo
COPY ./app.py /app.py
CMD ["python","-u", "app.py"]
