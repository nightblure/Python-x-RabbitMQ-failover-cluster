from src.utils import get_connection


def main():
    channel = get_connection().channel()
    channel.exchange_declare(exchange='ex', exchange_type='direct')
    channel.queue_declare(queue='q1', durable=True, arguments={'x-queue-type': 'classic'})
    channel.queue_bind(exchange='ex', queue='q1', routing_key='key')


if __name__ == '__main__':
    main()
