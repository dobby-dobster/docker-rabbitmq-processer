#!/usr/bin/env python3
import pika, random, string, time
from retry import retry

def random_generator(size=32, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

@retry()
def send_to_rabbit(random_string):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit'))
    channel = connection.channel()
    channel.queue_declare(queue='RandomStrings')
    channel.basic_publish(exchange='', routing_key='RandomStrings', body=random_string)
    print('Random string ({}) sent'.format(random_string))
    connection.close()

def main():
    while True:
      random_string = random_generator()
      print('Random string generated: {}'.format(random_string))
      send_to_rabbit(random_string)
      print('Sleeping for 1 seconds..')
      time.sleep(1)

main()
