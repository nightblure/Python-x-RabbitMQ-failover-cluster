#!/usr/bin/env python3
import time

import pika

from src.settings import FIRST_NODE_URL, SECOND_NODE_URL
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
    first_channel = get_broker_connection(FIRST_NODE_URL).channel()
    second_channel = get_broker_connection(SECOND_NODE_URL).channel()

    credentials = pika.PlainCredentials('admin', 'admin')
    parameters = pika.ConnectionParameters(host='localhost', port=8000, credentials=credentials)
    connection = pika.BlockingConnection(parameters)

    for i in range(1, 6):
        body = f'test msg №{i}'

        send_message(first_channel, body, 'ex1', 'key')
        time.sleep(1)
        send_message(second_channel, body, 'ex2', 'key')

    first_channel.close()
    second_channel.close()


if __name__ == '__main__':
    main()
