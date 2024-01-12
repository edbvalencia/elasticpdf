from datetime import datetime

from elasticsearch import Elasticsearch

es = Elasticsearch("http://elasticsearch:9200")

doc = {
    "author": "eduardo",
    "text": "Interesting content...",
    "timestamp": datetime.now(),
}


def save():
    resp = es.index(index="test-index", body=doc)
    print(resp["result"])
