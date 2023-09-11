from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)


@app.route('/')
def hello_world():
    return 'Hello, this is user management service'



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=False)
