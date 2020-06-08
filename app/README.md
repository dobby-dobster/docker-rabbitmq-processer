# docker-rabbitmq-processer

This is a docker deployment of RabbitMQ with Python producer and consumer.

## Deployment

1. Clone this repo
```bash
git clone https://github.com/dobby-dobster/docker-rabbitmq-processer.git
```
2. Deploy
```bash
docker-compose up -d
```
2. Validate
Three containers should now be running
  docker-rabbitmq-processer_rabbitmq_1
  docker-rabbitmq-processer_producer_1
  docker-rabbitmq-processer_consumer_1
```bash
docker container ls | grep docker-rabbitmq
```

## Containers
- docker-rabbitmq-processer_rabbitmq_1 - standard rabbitmq container
- docker-rabbitmq-processer_producer_1 - producer container, runs send.py which generates a 32 randaom character string and publishes message to queue (RandomStrings). Sleeps for 1 minute before publishing next message.
docker-rabbitmq-processer_consumer_1 - consumer container, runs fetch.py which consumes messages from the queue (RandomStrings).

Producer and consumer are based on centos8 image. A more efficent way would be to use a python image, however made testing more difficult.
