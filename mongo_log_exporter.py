from prometheus_client import start_http_server, Gauge
from pymongo import MongoClient
import time

log_count = Gauge('log_count_total', 'Total number of logs')
error_count = Gauge('log_error_total', 'Total error logs')

def fetch_metrics():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["ai_logs"]
    while True:
        logs = db.logs
        log_count.set(logs.count_documents({}))
        error_count.set(logs.count_documents({"level": "error"}))
        time.sleep(5)

if __name__ == "__main__":
    start_http_server(9200)  # Prometheus will scrape this
    fetch_metrics()
