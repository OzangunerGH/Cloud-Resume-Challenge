import os
from cloud_challenge.function.app import lambda_handler as lambda_handler

def test_lambda_handler():
    # Checking AWS Credentials
    assert "AWS_ACCESS_KEY_ID" in os.environ
    assert "AWS_SECRET_ACCESS_KEY" in os.environ
    response = lambda_handler("", "")
    response_2 = lambda_handler("", "")

    # assert return keys
    assert "statusCode" in response
    assert "headers" in response
    assert "body" in response

    # checking headers for CORS
    assert "Access-Control-Allow-Origin" in response["headers"]
    assert "Access-Control-Allow-Methods" in response["headers"]
    assert "Access-Control-Allow-Headers" in response["headers"]

    # checking status code
    assert response["statusCode"] == 200
    assert response_2["body"] == response["body"] + 1
        
test_lambda_handler()
