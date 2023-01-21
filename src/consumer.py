#!/usr/bin/env python3
import os
import pika
import sys

from src.settings import RABBITMQ_BROKER_URL


def on_message(ch, method, properties, body):
    print(f'Received: {body.decode()}')


def main():
    parameters = pika.URLParameters(RABBITMQ_BROKER_URL)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.basic_consume(queue='test', on_message_callback=on_message, auto_ack=True)
    print('\nWaiting for messages... (To exit press stop button)\n')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Stopped')
        sys.exit(0)
