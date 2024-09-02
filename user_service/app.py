from flask import Flask, request, jsonify
from user_data import create_user_table, register_user, validate_user
from common.kafka_service import KafkaService
from common.elasticsearch_service import ElasticsearchService

app = Flask(__name__)

# Veritabanı tablosunu oluştur
create_user_table()

# Kafka ve Elasticsearch servislerini başlat
kafka_service = KafkaService()
es_service = ElasticsearchService()

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    if register_user(data['username'], data['password']):
        log_data = {"service": "user_service", "message": "User registered", "level": "INFO"}
        kafka_service.send_log(topic="otel-logs", log_data=log_data)
        es_service.index_log(index="otel-logs", log_data=log_data)
        return jsonify({"status": "User registered"}), 201
    else:
        return jsonify({"status": "User registration failed"}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if validate_user(data['username'], data['password']):
        log_data = {"service": "user_service", "message": "User logged in", "level": "INFO"}
        kafka_service.send_log(topic="otel-logs", log_data=log_data)
        es_service.index_log(index="otel-logs", log_data=log_data)
        return jsonify({"status": "Login successful"}), 200
    else:
        return jsonify({"status": "Login failed"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
