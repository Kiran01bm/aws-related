# Simple HTTP Endpoint Example

Inspired by the [aws-node-simple-http-endpoint](https://github.com/serverless/examples/tree/master/aws-node-simple-http-endpoint), in Ruby!

## Setting up alarms
### serverless.yaml
```
serverless.yaml

service: serverless-ruby-simple-http-endpoint
 
frameworkVersion: ">=1.1.0 <2.0.0"
 
provider:
  name: aws
  runtime: ruby2.5
 
plugins:
  - serverless-plugin-aws-alerts
 
custom:
  alerts:
    stages:
      - production
    topics:
      alarm:
        topic: ${self:service}-${opt:stage}-alerts-alarm
        notifications:
          - protocol: email
            endpoint: INSERT_EMAIL
    alarms:
      - functionThrottles
      - functionErrors
      - functionInvocations
      - functionDuration
functions:
  sleeper:
    handler: handler.endpoint
    events:
      - http:
          path: ping
          method: get
```
### Deploy to Production Stage
```
~/Documents/python/examples/aws-ruby-simple-http-endpoint on  master! ⌚ 17:10:14
$ serverless deploy --stage production
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Creating Stack...
Serverless: Checking Stack create progress...
.....
Serverless: Stack create finished...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service rubysls.zip file to S3 (1.98 KB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
.......................................
Serverless: Stack update finished...
Service Information
service: rubysls
stage: production
region: us-east-1
stack: rubysls-production
resources: 13
api keys:
  None
endpoints:
  GET - https://91uc10usj2.execute-api.us-east-1.amazonaws.com/production/ping
functions:
  sleeper: rubysls-production-sleeper
layers:
  None
 
~/Documents/python/examples/aws-ruby-simple-http-endpoint on  master! ⌚ 17:11:56
```

### Deploy yoe Staging Stage
Note: Notice that the Alerts did not get created. See WARNING in the logs below which says - "Serverless: Warning: Not deploying alerts on stage staging"
```
~/Documents/python/examples/aws-ruby-simple-http-endpoint on  master! ⌚ 17:11:56
$ serverless deploy --stage staging
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Warning: Not deploying alerts on stage staging
Serverless: Creating Stack...
Serverless: Checking Stack create progress...
.....
Serverless: Stack create finished...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service rubysls.zip file to S3 (1.98 KB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
..............................
Serverless: Stack update finished...
Service Information
service: rubysls
stage: staging
region: us-east-1
stack: rubysls-staging
resources: 10
api keys:
  None
endpoints:
  GET - https://g3f5gr0fkk.execute-api.us-east-1.amazonaws.com/staging/ping
functions:
  sleeper: rubysls-staging-sleeper
layers:
  None
 
~/Documents/python/examples/aws-ruby-simple-http-endpoint on  master! ⌚ 17:20:39
$
```


## Use Cases

- Wrapping an existing internal or external endpoint/service

## Deploy 

In order to deploy the endpoint, simply run:

```bash
sls deploy
```

The expected result should be similar to:

```bash
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service .zip file to S3 (849 B)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
...............................
Serverless: Stack update finished...
Service Information
service: serverless-ruby-simple-http-endpoint
stage: dev
region: us-east-1
stack: serverless-ruby-simple-http-endpoint-dev
api keys:
  None
endpoints:
  GET - https://spmfbzc6ja.execute-api.us-east-1.amazonaws.com/dev/ping
functions:
  current_time: serverless-ruby-simple-http-endpoint-dev-current_time
layers:
  None
Serverless: Removing old service artifacts from S3...
```
## Usage

Send an HTTP request directly to the endpoint using a tool like curl:

```bash
curl https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/ping
```

## Scaling

By default, AWS Lambda limits the total concurrent executions across all functions within a given region to 100. The default limit is a safety limit that protects you from costs due to potential runaway or recursive functions during initial development and testing. To increase this limit above the default, follow the steps in [To request a limit increase for concurrent executions](http://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html#increase-concurrent-executions-limit).
