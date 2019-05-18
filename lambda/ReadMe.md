# General for Lamda

## CloudWatch Metrics
1. **Invocations:** The number of times your function is invoked;
2. **Errors:** The number of times your function fails with an error, due to timeouts, memory issues, unhandled exceptions, or other issues;
3. **Throttles:** The number of times your function is throttled. AWS limits the concurrent number of executions across all your functions. If you exceed that, your function will be throttled and won't be allowed to run.
4. **Duration:** How long your function runs.

## Samples

Deploy
```
serverless deploy

```
Remove: Remove resources directly ex: Remove from CloudFormation etc etc
```
serverless remove
```


