import boto3
import os

client = boto3.client('cloudfront')

def lambda_handler(event, context):

    distribution_id = os.environ['DISTRIBUTION_ID']

    try:
        response = client.create_invalidation(
            DistributionId=distribution_id,
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
            "body": "Invalidation created",
            "invalidation_id": response['Invalidation']['Id']
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "error": str(e)
        }