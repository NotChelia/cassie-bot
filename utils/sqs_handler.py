import boto3
import json
import logging

logger = logging.getLogger(__name__)

sqs_client = boto3.client('sqs', region_name='us-east-2')
sqs_queue_url = "https://sqs.us-east-1.amazonaws.com/905418150353/scraper-queue"

def receive_sqs_messages():
    """
    Poll the SQS queue for new messages.
    """
    try:
        response = sqs_client.receive_message(
            QueueUrl=sqs_queue_url,
            MaxNumberOfMessages=5,
            WaitTimeSeconds=20
        )
        return response.get('Messages', [])
    except Exception as e:
        logger.error(f"Error while receiving messages from SQS: {e}")
        return []

def delete_sqs_message(receipt_handle):
    """
    Delete a message from the SQS queue after processing.
    """
    try:
        sqs_client.delete_message(
            QueueUrl=sqs_queue_url,
            ReceiptHandle=receipt_handle
        )
    except Exception as e:
        logger.error(f"Error while deleting message from SQS: {e}")

def process_sqs_message(message):
    """
    Process the SQS message and extract chapter details.
    """
    try:
        body = json.loads(message['Body'])
        chapter_no = body['chapter_no']
        chapter_title = body['chapter_title']
        chapter_url = body['chapter_url']
        return chapter_no, chapter_title, chapter_url
    except Exception as e:
        logger.error(f"Error processing message from SQS: {e}")
        return None, None, None
