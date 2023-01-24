#!/usr/bin/env python3
import sys

from src.settings import SECOND_NODE_URL
from src.utils import start_consuming


def on_receive_msg_callback(channel, method, properties, body):
    print(f'Received: {body.decode()}')


def main():
    start_consuming(SECOND_NODE_URL, 'q2', on_receive_msg_callback)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Stopped')
        sys.exit(0)
