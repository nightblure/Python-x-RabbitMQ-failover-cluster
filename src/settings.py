import os

RABBITMQ_HOST = 'rabbitmq_node_1' if 'FROM_DOCKER_COMPOSE' in os.environ else 'localhost'

FIRST_NODE_PORT = 5670
FIRST_NODE_URL = f'amqp://admin:admin@{RABBITMQ_HOST}:{FIRST_NODE_PORT}'

SECOND_NODE_PORT = 5671
SECOND_NODE_URL = f'amqp://admin:admin@{RABBITMQ_HOST}:{SECOND_NODE_PORT}'
