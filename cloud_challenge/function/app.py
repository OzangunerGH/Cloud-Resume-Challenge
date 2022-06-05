import boto3


dynamodb = boto3.resource('dynamodb')
ddbTableName = 'VisitorCount'
table = dynamodb.Table(ddbTableName)


def lambda_handler(event, context):
    # Update item in table or add if doesn't exist
    ddbResponse = table.update_item(
        Key={'ID': 'count'},
        UpdateExpression='ADD #att :val1',  
        ConditionExpression="attribute_not_exists(#a)",
        ExpressionAttributeNames={"#att": "visitor_count", "#a": "attribute"}, 
        ExpressionAttributeValues={
            ':val1': 1
        },
        ReturnValues="UPDATED_NEW")

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
