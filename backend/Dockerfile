FROM python
RUN pip install flask requests prometheus-flask-exporter pymongo
COPY ./app.py /app.py
CMD ["python", "app.py"]
