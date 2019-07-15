# General Notes

## Services:
1. SQS - Fully managed Message Queueing Services
2. SNS - Fully managed Pub/Sub service
3. Step Functions - Orchestration of Functions in Distributed systems.
4. SWF - Simple Workflow


## SQS:
	Queue for Storing Messages and it Pull based. Consumers Pull the messages.
	Messages can be 1kb to 256kb
	SQS --> Cloudwatch --> Autoscale --> EC2 == This is to use SQS to trigger autoscaling
	Types
		1. Standard Queue - Nearly unlimited TPS, Best Effort in Ordering, Chances of Duplicates so Application to handle checks and balances for more than once delivery.
		2. FIFO - 300 Transactions per second, First in First Out so ordered delivery, Exactly Once delivery.
	Visibility Timeout Period 
		- The period for which the message is not visible after a Reader picks up the message.
		- Default visibility timeout is 12 hours.
	Dead Letter Queue
	Delay Queues - Postpone Delivery of new messages - Message is not visible in the queue after being added to the queue for the Delay seconds
	Polling Types
		Short Polling
		Long Polling - By setting ReceiveMessageWaitTime for more than 0 seconds. By doing this we wait till the message arrives in the Queue or the ReceiveMessageWaitTime times-up
	Message retention can be configured from 1 minute to 14 days. Default is 4 days. Messages are automatically deleted after the retention period ends.

## SNS:
	Enables sending messages of upto 256kb
	Topic
	Content on SNS is stored redundantly across multiple AZs
	You can send message to Topic via Console, CLI, SDK
	Subscribers subscribe to the Topic and Subscribers access to the Topic is governed by Access Policies.
	Transport Protocols
		HTTP
		Email
		SQS
		SMS
		Mobile Push - No Polling

## Simple Workflow:
	Workflow is the control flow logic for the execution of Tasks
	Co-ordinate work across multiple distributed applications
	A domain contains a Workflow or Workflows
	Task - Can be run serially, parallely.. upon Manual approval or automatically after execution of previous tasks.
	Actors interact with SWF to coordinate tasks.
	Ensures that tasks are executed only once - One time only execution is a Key feature of SWF
	Workflow execution can last upto 1 year.
	SWF is API based and can be accessed with a wide range of programming languages which has SWF SDKs
	Workflow Actors:
		Workflow Starters - A application that initiates the workflow
		Deciders - Control the flow logic
		Activity Workers - Carry out the tasks
