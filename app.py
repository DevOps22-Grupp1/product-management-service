from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)


metrics.info("app_info", "order-processing-service", version="1.0.0")


@metrics.counter(
    "invocation_by_method",
    "Number of invocations by HTTP method",
)
@app.route("/")
def hello_world():
    return "Goodbye, World!"


# Very important to disable debug mode
app.run(host="0.0.0.0", port=5003, debug=False)
