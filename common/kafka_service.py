from kafka import KafkaProducer
import json

class KafkaService:
    def __init__(self, broker_url='kafka:9092'):
        self.producer = KafkaProducer(
            bootstrap_servers=[broker_url],
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            api_version_auto_timeout_ms=30000  # 30 saniye timeout
        )

    def send_log(self, topic, log_data):
        """Kafka'ya log gönderir."""
        self.producer.send(topic, log_data)
        self.producer.flush()
