from flask import Flask, jsonify, send_from_directory
import requests

app = Flask(__name__, static_url_path='/static')

services = {
    "airflow": {
        "name": "Apache Airflow",
        "capability": "Workflow Orchestration",
        "dashboard_url": "http://localhost:8089"
    },
    "kafka": {
        "name": "Apache Kafka",
        "capability": "Event Streaming Platform",
        "dashboard_url": "#"
    },
    "mage": {
        "name": "Mage",
        "capability": "Data Orchestration",
        "dashboard_url": "http://localhost:6789"
    },
    "jenkins": {
        "name": "Jenkins",
        "capability": "CI/CD Automation",
        "dashboard_url": "http://localhost:8080"
    },
    "flink": {
        "name": "Apache Flink",
        "capability": "Stream Processing",
        "dashboard_url": "http://localhost:8081"
    },
    "grafana": {
        "name": "Grafana",
        "capability": "Metrics Visualization",
        "dashboard_url": "http://localhost:3000"
    },
    "postgres": {
        "name": "PostgreSQL",
        "capability": "Relational Database",
        "dashboard_url": "#"
    }
}

@app.route('/')
def root():
    return send_from_directory('static', 'index.html')

@app.route('/api/status/all')
def status():
    statuses = {}
    for key, svc in services.items():
        try:
            resp = requests.get(svc["dashboard_url"], timeout=1) if "http" in svc["dashboard_url"] else None
            statuses[key] = {**svc, "status": "online" if resp and resp.ok else "offline"}
        except:
            statuses[key] = {**svc, "status": "offline"}
    return jsonify(statuses)

@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
