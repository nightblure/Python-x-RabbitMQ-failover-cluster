#!/usr/bin/env python3
import time

import pika

from src.settings import RMQ_ADMIN_LOGIN, RMQ_ADMIN_PASSWORD
from src.utils import get_connection, send_message

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
    print(RMQ_ADMIN_LOGIN, RMQ_ADMIN_PASSWORD)
    channel = get_connection('localhost', 5672, RMQ_ADMIN_LOGIN, RMQ_ADMIN_PASSWORD).channel()

    # for i in range(1, 6):
    #     body = f'test msg №{i}'
    #     send_message(channel, body, 'ex1', 'key')
    #     time.sleep(1)
    #
    # channel.close()


if __name__ == '__main__':
    main()
