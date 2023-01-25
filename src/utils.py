import pika

from src.settings import LOAD_BALANCER_PORT, LOAD_BALANCER_HOST, RMQ_ADMIN_PASSWORD, RMQ_ADMIN_LOGIN


def get_broker_connection(broker_url):
    parameters = pika.URLParameters(broker_url)
    connection = pika.BlockingConnection(parameters)
    return connection


def _get_connection(host, port, login, password):
    credentials = pika.PlainCredentials(login, password)
    parameters = pika.ConnectionParameters(host=host, port=port, credentials=credentials)
    connection = pika.BlockingConnection(parameters)
    return connection


def send_message(channel, body, exchange, routing_key):
    encoded_body = str.encode(body, encoding='utf-8')
    channel.basic_publish(exchange=exchange, routing_key=routing_key, body=encoded_body)
    print(f"Sent '{body}'")


def start_consuming(channel, queue, on_receive_msg_callback):
    channel.basic_consume(queue=queue, on_message_callback=on_receive_msg_callback, auto_ack=True)
    print('\nWaiting for messages... (To exit press stop button)\n')
    channel.start_consuming()


def get_connection():
    return _get_connection(
        LOAD_BALANCER_HOST,
        LOAD_BALANCER_PORT,
        RMQ_ADMIN_LOGIN,
        RMQ_ADMIN_PASSWORD
    )
