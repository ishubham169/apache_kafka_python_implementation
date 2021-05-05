# importing kafka producer
from kafka.producer import KafkaProducer
import json

# Add kafka-server host and port (docker hostname)
server = "kubernetes.docker.internal:9092"


kafka_producer = KafkaProducer(bootstrap_servers=server)

# Kafka Topic that we have created in previous step
topic = "Users"

# Data to be send to Kafka
data = {"name": "Shubham Kaushik", "profession": "Software Developer"}

# Sending Data
kafka_producer.send(topic, json.dumps(data, indent=2).encode('utf-8'))

kafka_producer.flush()
