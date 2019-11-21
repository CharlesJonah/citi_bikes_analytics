import json

PRODUCER_CONFIGS = {
    "bootstrap_servers":['localhost:9098'],
    "value_serializer":lambda v: json.dumps(v).encode('utf-8'),
}