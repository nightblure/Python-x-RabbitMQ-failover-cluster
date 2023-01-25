#!/usr/bin/env python3
import sys

from retry import retry

from src.utils import start_consuming, get_connection


def on_receive_msg_callback(channel, method, properties, body):
    print(f'Received: {body.decode()}')


@retry(Exception, delay=3)
def main():
    channel = get_connection().channel()

    try:
        start_consuming(channel, 'q1', on_receive_msg_callback)
    except KeyboardInterrupt:
        print('Stopped')
        sys.exit(0)
    finally:
        channel.close()


if __name__ == '__main__':
    main()

