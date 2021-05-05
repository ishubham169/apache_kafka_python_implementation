# importing kafka producer
from kafka.consumer import KafkaConsumer
import json

# Add kafka-server host and port (docker hostname)
server = "kubernetes.docker.internal:9092"

# Kafka Topic that our Kafka Consumer is subscribing.
topic = "Users"

consumer = KafkaConsumer(topic, bootstrap_servers=server)

# Consuming Data and when we received data we are printing it to console
try:
    for msg in consumer:
        if msg.value:
            print("Data Received", json.loads(msg.value))
finally:
    # Close down consumer to commit final offsets.
    consumer.close()
