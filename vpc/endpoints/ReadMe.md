## Interface Endpoint (AWS Private Link)
An interface endpoint is an elastic network interface with a private IP address from the IP address range of your subnet that serves as an entry point for traffic destined to a supported service.

## Gateway Endpoint 
A gateway endpoint is a gateway that you specify as a target for a route in your route table for traffic destined to a supported AWS service. Only S3 and DynamoDB are supported

For RDS and Elasticache we cannot use VPC Endpoints (be it Interface Endpoints - AWS Private Link or Gateway Endpoint)


## NAT Gateway, Internet Gateway, Gateway Endpoint (for S3 and DynamoDB)
1. Whether a subnet is private or public depends on its route table. A public subnet has a route pointing to an internet gateway, and a private subnet does not.
2. Private Subnets Route Table - Route entry 0.0.0.0/0 will point to NatGateway (NatGateway resides in the Public Subnet).
3. Public Subnets route Table - Route entry 0.0.0.0/0 will point to the Internet Gateway.
4. A Gateway Endpoint is a gateway that you specify as a target for a route in your route table for traffic destined to a supported AWS service i.e S3 and DynamoDB.

