import boto3
import json


# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='Qone')
q1 = 'https://sqs.us-east-1.amazonaws.com/437652894623/q1'

# send messsage to the queue
response = queue.send_message(QueueUrl=q1, MessageBody='Hello there I'm sending messsage ... ')