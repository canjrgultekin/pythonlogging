from flask import Flask, request, jsonify
from reservation_data import create_reservation_table, add_reservation, get_all_reservations
from common.kafka_service import KafkaService
from common.elasticsearch_service import ElasticsearchService

app = Flask(__name__)

# Veritabanı tablosunu oluştur
create_reservation_table()

# Kafka ve Elasticsearch servislerini başlat
kafka_service = KafkaService()
es_service = ElasticsearchService()

@app.route('/reservations', methods=['POST'])
def create_reservation():
    data = request.json
    add_reservation(data['user_id'], data['hotel_id'], data['date'])
    log_data = {"service": "reservation_service", "message": "Reservation made", "level": "INFO"}
    kafka_service.send_log(topic="otel-logs", log_data=log_data)
    es_service.index_log(index="otel-logs", log_data=log_data)
    return jsonify({"status": "Reservation made"}), 201

@app.route('/reservations', methods=['GET'])
def list_reservations():
    reservations = get_all_reservations()
    return jsonify({"reservations": reservations}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
