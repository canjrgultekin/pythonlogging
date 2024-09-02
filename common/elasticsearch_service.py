from elasticsearch import Elasticsearch

class ElasticsearchService:
    def __init__(self, host='elasticsearch', port=9200):
        self.es = Elasticsearch([{'host': host, 'port': port, 'scheme': 'http'}])

    def index_log(self, index, log_data):
        """Elasticsearch'e log gönderir."""
        self.es.index(index=index, body=log_data)
