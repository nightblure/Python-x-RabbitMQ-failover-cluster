import pika


def get_broker_connection(broker_url):
    parameters = pika.URLParameters(broker_url)
    connection = pika.BlockingConnection(parameters)
    return connection


def send_message(channel, body, exchange, routing_key):
    encoded_body = str.encode(body, encoding='utf-8')
    channel.basic_publish(exchange=exchange, routing_key=routing_key, body=encoded_body)
    print(f"Sent '{body}'")


def start_consuming(broker_url, queue, on_receive_msg_callback):
    channel = get_broker_connection(broker_url).channel()
    channel.basic_consume(queue=queue, on_message_callback=on_receive_msg_callback, auto_ack=True)
    print('\nWaiting for messages... (To exit press stop button)\n')
    channel.start_consuming()
