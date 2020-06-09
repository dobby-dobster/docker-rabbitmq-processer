#!/usr/bin/env python3
import pika
from retry import retry

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

@retry()
def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit'))
    channel = connection.channel()
    channel.queue_declare(queue='RandomStrings')
    channel.basic_consume(queue='RandomStrings', on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

main()