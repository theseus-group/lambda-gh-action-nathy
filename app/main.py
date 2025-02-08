import random

def lambda_handler(event, context):
    random_number = random.randint(0, 100)
    print(f"Generated Random Number: {random_number}")

    return {
        "statusCode": 200,
        "body": f"{{\"random_number\": {random_number}}}"
    }
