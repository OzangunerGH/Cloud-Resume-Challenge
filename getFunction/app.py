import boto3


dynamodb = boto3.resource('dynamodb')
ddbTableName = 'VisitorCount'
table = dynamodb.Table(ddbTableName)


def lambda_handler(event, context):
    # Update item in table or add if doesn't exist
    ddbResponse = table.update_item(
        Key={'id': 'count'},
        UpdateExpression='SET visitor_count = visitor_count + :val1',
        ExpressionAttributeValues={
            ':val1': 1
        },
        ReturnValues="UPDATED_NEW"
    )

    # Format dynamodb response into variable

    # Create api response object
    apiResponse = {
        "isBase64Encoded": False,
        "statusCode": 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
        },
        'body': int(ddbResponse['Attributes']['visitor_count'])
    }

    return apiResponse
