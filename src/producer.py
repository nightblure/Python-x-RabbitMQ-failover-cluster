#!/usr/bin/env python3
import os

import pika
import time

from src.settings import RABBITMQ_BROKER_URL

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
    parameters = pika.URLParameters(f'http://localhost:443/') # RABBITMQ_BROKER_URL
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    for i in range(5):
        body = f'test msg №{i}'
        encoded_body = str.encode(body, encoding='utf-8')
        channel.basic_publish(exchange='test', routing_key='key1', body=encoded_body)
        print(f"Sent '{body}'")

    connection.close()


if __name__ == '__main__':
    main()
