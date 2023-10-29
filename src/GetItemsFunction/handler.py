import json
import os
import boto3
import uuid

TABLE_NAME = os.environ["ITEMSTABLE_TABLE_NAME"]

ddb = boto3.resource("dynamodb")
table = ddb.Table(TABLE_NAME)

def handler(event, context):
    response = table.scan()

    return {
        "statusCode": 200,
        "body": json.dumps(response["Items"])
    }