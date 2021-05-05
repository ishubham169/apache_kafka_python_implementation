# importing required packages
from kafka.admin import KafkaAdminClient, NewTopic

# Add kafka-server host and port (docker hostname)
server = "shubham-mac:9092"
kafka_admin = KafkaAdminClient(bootstrap_servers=server)

# Creating a new Kafka-topic = Users
topic_list = list()
topic_list.append(NewTopic(name="Users", num_partitions=1, replication_factor=1))
kafka_admin.create_topics(new_topics=topic_list, validate_only=False)
