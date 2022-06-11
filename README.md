# Cloud-Resume-Challenge
Cloud Resume Challenge

This is a implementation of the #CloudResumeChallenge on AWS using a Serverless architecture.

You can view the end result at www.ozangunercloud.ga

![Alt text](https://ibb.co/Y2t5XxM)


To deploy SAM template to stack, apply following commands : 

sam build
sam deploy

To upload/update website files to your S3 bucket, use this command

aws s3 cp yourpathtowebsitefiles/. s3://yourbucketname/ --recursive

Currently these steps are implemented through GitHub actions.
