#!/usr/bin/env python3
import sys
import time

from pika.exceptions import ConnectionClosedByBroker
from retry import retry

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


@retry(Exception, delay=3)
def main():
    channel = get_connection().channel()

    try:

        for i in range(1, 101):
            body = f'test msg №{i}'
            send_message(channel, body, 'ex', 'key')
            time.sleep(1)
            i += 1

    except KeyboardInterrupt:
        print('Stopped')
        sys.exit(0)
    except ConnectionClosedByBroker:
        print('Try to reconnect...')
    finally:
        channel.close()


if __name__ == '__main__':
    main()
