## SQS Observability

### NumberOfMessagesSent - Producer Health
This metric measures the number of messages enqueued in a 5 minute interval. It can be useful for determining the health of the systems sending data to SQS. Watch this metric to make sure your producer doesn’t suddenly start sending more messages, or stop sending messages completely.


### ApproximateAgeOfOldestMessage - Consumer Health
ApproximateAgeOfOldestMessage measures the number of seconds since the creation of the oldest message in the queue. This metric is effective because if it creeps up, it means that messages are not being processed quickly enough. If you don’t have a redrive policy set for your queue, it also alerts you to messages that your consumers can’t handle and that are stuck in your queue.


### ApproximateNumberOfMessagesNotVisible - Mismatch between Consumer and Producer speed/health
Inflight messages are the messages that have been received by a consumer, but have not been deleted or failed. In other words, they are actively being processed. For a standard SQS queue, there is a limit of 120,000 inflight messages, and and 20,000 is the limit for FIFO queues. This alerts when the Maximum aggregation exceeds 110,000 messages for a standard queue or 18,000 for FIFO queues.


### ApproximateNumberOfMessagesVisible - DLQ
When a message repeatedly fails to be processed, it can be sent to a configured dead letter queue. Unfortunately, in many cases DLQs are forgotten about and messages sent there disappear into the void. To avoid this problem, you’ll need to watch the ApproximateNumberOfMessagesVisible metric for the DLQ.

Unfortunately, in a somewhat counterintuitive way, messages being sent to the DLQ as a result of failing in the original queue do not increment NumberOfMessagesSent and hence NumberOfMessagesSent cannot be used for DLQ.
