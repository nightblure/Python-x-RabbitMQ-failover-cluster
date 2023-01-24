#!/usr/bin/env python3
import time

import pika

from src.settings import FIRST_NODE_URL
from src.utils import get_broker_connection, send_message

"""

Общие принципы работы RabbitMQ:

1. создаются сущности exchange разного типа (см. ниже) и для них привязываются очереди

Типы exhange:

* direct - доставка и получение сообщений осуществляются
    на основе соответствия у продюсера и консьюмера имени очереди и ключа маршрутизации (routing_key)

* fanout - доставка и получение сообщений осуществляются 
    на основе соответствия у продюсера и консьюмера имени очереди (routing_key не важен)

* topic - доставка и получение сообщений осуществляются 
    на основе соответствия у продюсера и консьюмера имени очереди и routing_key по регулярному выражению

"""


def main():
    # channel = get_broker_connection(FIRST_NODE_URL).channel()

    credentials = pika.PlainCredentials('admin', 'admin')
    parameters = pika.ConnectionParameters(host='localhost', port=5673, credentials=credentials)
    connection = pika.BlockingConnection(parameters)

    # for i in range(1, 6):
    #     body = f'test msg №{i}'
    #     send_message(channel, body, 'ex1', 'key')
    #     time.sleep(1)
    #
    # channel.close()


if __name__ == '__main__':
    main()
