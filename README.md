# Cloud-Resume-Challenge


This is a implementation of the #CloudResumeChallenge on AWS using a Serverless Architecture.

You can view the outcome of the challenge at **www.ozangunercloud.ga**

You can read more about my experience with the challenge **[here](https://dev.to/ozanguner/the-cloud-resume-challenge-27cd)**



![Alt text](https://i.imgur.com/SPXgoSd.png)

To deploy SAM template to stack, apply following commands : 

sam build

sam deploy

To upload/update website files to your S3 bucket, use this command

aws s3 cp yourpathtowebsitefiles/. s3://yourbucketname/ --recursive

Currently these steps are implemented through GitHub actions and applied after tests are successful.
