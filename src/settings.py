import os
from pathlib import Path

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = ROOT_DIR / '.envs'

load_dotenv(ENV_PATH)

RMQ_ADMIN_LOGIN = os.environ['RMQ_ADMIN_LOGIN']
RMQ_ADMIN_PASSWORD = os.environ['RMQ_ADMIN_PASSWORD']

LOAD_BALANCER_HOST = 'haproxy' if 'FROM_DOCKER_COMPOSE' in os.environ else 'localhost'
LOAD_BALANCER_PORT = os.environ['LOAD_BALANCER_PORT']

# FIRST_NODE_URL = f'amqp://{ADMIN_LOGIN}:{ADMIN_PASSWORD}@{RABBITMQ_HOST}:{FIRST_NODE_PORT}'
