
def lambda_handler(event, context):
    print("Processing receipt...")
    return {"statusCode": 200, "body": "Receipt processed successfully!"}
