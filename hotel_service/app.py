from flask import Flask, request, jsonify
from hotel_data import create_hotel_table, add_hotel, get_all_hotels
from common.kafka_service import KafkaService
from common.elasticsearch_service import ElasticsearchService

app = Flask(__name__)

# Veritabanı tablosunu oluştur
create_hotel_table()

# Kafka ve Elasticsearch servislerini başlat
kafka_service = KafkaService()
es_service = ElasticsearchService()

@app.route('/hotels', methods=['POST'])
def create_hotel():
    data = request.json
    add_hotel(data['name'], data['location'])
    log_data = {"service": "hotel_service", "message": "Hotel added", "level": "INFO"}
    kafka_service.send_log(topic="otel-logs", log_data=log_data)
    es_service.index_log(index="otel-logs", log_data=log_data)
    return jsonify({"status": "Hotel added"}), 201

@app.route('/hotels', methods=['GET'])
def list_hotels():
    hotels = get_all_hotels()
    return jsonify({"hotels": hotels}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
