#!/bin/bash

# Wait for RabbitMQ to start
sleep 10

# Create the four topics
rabbitmqadmin declare exchange name=estoque type=topic
rabbitmqadmin declare exchange name=pagamentos type=topic
rabbitmqadmin declare exchange name=pedidos type=topic
rabbitmqadmin declare exchange name=produtos type=topic

echo "RabbitMQ topics created successfully"
