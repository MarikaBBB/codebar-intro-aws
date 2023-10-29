import json

def handler(event, context):
    # Log the event argument for debugging and for use in local development.
    print(json.dumps(event))

    return {
        "statusCode": 200,
        "body": json.dumps([
            {"id": "1", "title": "Attend codebar talk"}
        ])
    }
