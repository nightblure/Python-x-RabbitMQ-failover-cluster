import os

RABBITMQ_HOST = 'rabbitmq_node_1' if 'FROM_DOCKER_COMPOSE' in os.environ else 'localhost'
RABBITMQ_PORT = 5670
RABBITMQ_BROKER_URL = f'amqp://admin:admin@{RABBITMQ_HOST}:{RABBITMQ_PORT}'
