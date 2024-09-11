import boto3
from botocore.exceptions import ClientError

class ServerConfigManager:
    def __init__(self, region_name="us-east-2"):
        self.dynamodb = boto3.resource('dynamodb', region_name=region_name)
        self.table = self.dynamodb.Table('ServerConfigs')

    def get_server_config(self, server_id):
        try:
            response = self.table.get_item(Key={'server_id': server_id})
            if 'Item' not in response:
                default_config = {
                    "server_id": server_id,
                    "is_checking_updates": False,
                    "subscribed_roles": [],
                    "post_channel_id": None,
                    "URL": "https://www.lightnovelworld.co/novel/shadow-slave-05122222/chapters?chorder=desc",
                    "last_notified_chapters": []
                }
                self.update_server_config(server_id, default_config)
                return default_config
            return response['Item']
        except ClientError as e:
            print(f"Unable to retrieve server config: {e.response['Error']['Message']}")
            return None

    def update_server_config(self, server_id, config):
        try:
            self.table.put_item(Item={"server_id": server_id, **config})
        except ClientError as e:
            print(f"Unable to update server config: {e.response['Error']['Message']}")
