import app
import os

def test_lambda_handler():
    # Checking AWS Credentials
    assert "AWS_ACCESS_KEY_ID" in os.environ
    assert "AWS_SECRET_ACCESS_KEY" in os.environ
    response = app.lambda_handler("", "")
    response_2 = app.lambda_handler("", "")

    # assert return keys
    assert "statusCode" in response
    assert "header" in response
    assert "body" in response

    # checking headers for CORS
    assert "Access-Control-Allow-Origin" in response["headers"]
    assert "Access-Control-Allow-Methods" in response["headers"]
    assert "Access-Control-Allow-Headers" in response["headers"]

    # checking status code
    if response["statusCode"] != 200 or response_2["body"] != response["body"] + 1:
        return exit(1)
    else:
        return exit(0)
        
test_lambda_handler()
