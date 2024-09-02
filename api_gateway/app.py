from flask import Flask, jsonify, request
import requests
from common.kafka_service import KafkaService
from common.elasticsearch_service import ElasticsearchService

app = Flask(__name__)

# Kafka ve Elasticsearch servislerini başlat
kafka_service = KafkaService()
es_service = ElasticsearchService()

# Mikroservis URL'leri
MICROSERVICES = {
    "user": "http://user_service:5000",
    "hotel": "http://hotel_service:5001",
    "reservation": "http://reservation_service:5002"
}


@app.route('/<service_name>/<action>', methods=['GET', 'POST'])
def call_service(service_name, action):
    if service_name not in MICROSERVICES:
        return jsonify({"error": "Service not found"}), 404

    service_url = f"{MICROSERVICES[service_name]}/{action}"

    try:
        if request.method == 'POST':
            response = requests.post(service_url, json=request.json)
        else:
            response = requests.get(service_url)

        log_data = {
            "service": "api_gateway",
            "message": f"Called {service_name} service action: {action}",
            "level": "INFO"
        }
        kafka_service.send_log(topic="otel-logs", log_data=log_data)
        es_service.index_log(index="otel-logs", log_data=log_data)

        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        log_data = {
            "service": "api_gateway",
            "message": f"Failed to call {service_name} service action: {action}, Error: {str(e)}",
            "level": "ERROR"
        }
        kafka_service.send_log(topic="otel-logs", log_data=log_data)
        es_service.index_log(index="otel-logs", log_data=log_data)

        return jsonify({"error": "Failed to call service"}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
