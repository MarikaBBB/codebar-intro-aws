import json
import os
import boto3
import uuid

TABLE_NAME = os.environ["ITEMSTABLE_TABLE_NAME"]

ddb = boto3.resource("dynamodb")
table = ddb.Table(TABLE_NAME)

def handler(event, context):
    # Log the event argument for debugging and for use in local development.
    print(json.dumps(event))

    item_id = str(uuid.uuid4())
    item_title = event["body"]

    table.put_item(
        Item={
            "id": item_id,
            "title": item_title
        }
    )

    return {
        "statusCode": 200,
        "body": "Item created."
    }
