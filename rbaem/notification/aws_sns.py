import boto3
from django.conf import settings


def create_topic(topic_name):
    client = boto3.client('sns', region_name=settings.AWS_REGION)

    response = client.create_topic(Name=topic_name)
    topic_arn = response['TopicArn']

    return topic_arn
#
#
def subscribe_to_topic(topic_arn, endpoint, protocol='sms'):
    client = boto3.client('sns', region_name=settings.AWS_REGION)

    response = client.subscribe(
        TopicArn=topic_arn,
        Protocol=protocol,
        Endpoint=endpoint
    )

    return response['SubscriptionArn']
#
#
# def send_message_to_topic(topic_arn, message):
#     client = boto3.client('sns', region_name=settings.AWS_REGION)
#
#     response = client.publish(
#         TopicArn=topic_arn,
#         Message=message,
#     )
#
#     return response['MessageId']

def send_sms(message, phone_number):
    client = boto3.client('sns', region_name=settings.AWS_REGION)

    response = client.publish(
        PhoneNumber=phone_number,
        Message=message,
    )

    return response['MessageId']