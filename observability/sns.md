## SNS Related

## NumberOfMessagesPublished
Inbound traffic to SNS. This metric tracks all the messages that have been published to the topic.

## NumberOfNotificationsDelivered
Outbound traffic from SNS. This metric tracks all the messages that have been successfully delivered to endpoints subscribed to the topic. A delivery takes place either when the incoming message attributes match a subscription filter policy, or when the subscription has no filter policy at all, which results in a catch-all behavior.

## NumberOfNotificationsFilteredOut
This metric tracks all the messages that were filtered out because they carried attributes that didn’t match the subscription filter policy.

## NumberOfNotificationsFilteredOut-NoMessageAttributes
This metric tracks all the messages that were filtered out because they didn’t carry any attributes at all and, consequently, didn’t match the subscription filter policy.

## NumberOfNotificationsFilteredOut-InvalidAttributes
This metric keeps track of messages that were filtered out because they carried invalid or malformed attributes and, thus, didn’t match the subscription filter policy.

## NumberOfNotificationsFailed
This last metric tracks all the messages that failed to be delivered to subscribing endpoints, regardless of whether a filter policy had been set for the endpoint. This metric is emitted after the message delivery retry policy is exhausted, and SNS stops attempting to deliver the message. At that moment, the subscribing endpoint is likely no longer reachable. For example, the subscribing SQS queue or Lambda function has been deleted by its owner. You may want to closely monitor this metric to address message delivery issues quickly.
