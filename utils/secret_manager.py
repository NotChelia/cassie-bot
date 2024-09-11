import boto3
from botocore.exceptions import ClientError
import json
import logging

def get_secret(secret_name="bot_token", region_name="us-east-2"):
    """
    Retrieve a secret from AWS Secrets Manager and extract the BOT_TOKEN.
    """
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
        secret = get_secret_value_response['SecretString']
        
        secret_dict = json.loads(secret)
        return secret_dict["BOT_TOKEN"]
        
    except ClientError as e:
        logging.error(f"Unable to retrieve secret {secret_name}: {e}")
        raise e
