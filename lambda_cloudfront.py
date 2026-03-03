import boto3

client = boto3.client('cloudfront')

def lambda_handler(event, context):
    response = client.create_invalidation(
        DistributionId='E123456789ABC',  # Replace with your Distribution ID
        InvalidationBatch={
            'Paths': {
                'Quantity': 1,
                'Items': ['/*']
            },
            'CallerReference': context.aws_request_id
        }
    )
    
    return {
        "statusCode": 200,
        "body": "Invalidation Created"
    }