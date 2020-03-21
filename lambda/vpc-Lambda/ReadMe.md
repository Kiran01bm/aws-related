## Lambda Inside VPC Considerations

1. By default, Lambda runs your functions in a secure VPC with access to AWS services (ex: Cognito, DynamoDB, SQS, SNS etc) and the Internet. The VPC is owned by Lambda and does not connect to your account's default VPC. 

2. When you connect a function to a VPC in your account, it does not have access to the internet or AWS Services unless your VPC provides access i.e For Internet Access and Access to AWS Services (ex: Cognito, DynamoDB, SQS, SNS etc) - NAT GW and IGW. For access to services in your VPC ex: RDS or Elasticache its sufficient if your Lambda is just VPC enabled.

3. Official statement from AWS - "Don’t put your Lambda function in a VPC unless you have to.."

4. VPC-enabled Lambda functions can access resources inside the designated VPC - The Function's runtime needs an Elastic Network Interface (ENI).

5. VPC-enabled Lambda functions are allowed to stay idle for longer to increase the likelihood that existing ENIs are reused.

6. VPCs impose serious scalability and performance limitations on Lambda functions.

7. ENIs are shared across containers. If a function is allocated with 1GB of memory, then up to three (3) containers running this function can share the same ENI.

8. Idle containers are usually garbage collected after a few minutes. VPC-enabled functions are allowed to stay idle for longer to increase the likelihood that existing ENis are reused.

9. ENI Soft Limits is 350 Per Region at 350 VPC-enabled functions will be throttled. 

10. Consider using dedicated subnets with large IP ranges for your Lambda functions.
```
Each ENI consumes a private IP address from the associated subnet, and each subnet has a limited number of available IP addresses based on its CIDR block. It’s therefore possible to exhaust the available IP addresses in a subnet when Lambda functions scale up quickly.
```

11. A VPC-enabled function would lose internet access because its ENI is only associated with a private IP address from the subnet. 
```
If your function needs to talk to other AWS services that are outside the VPC, such as DynamoDB or SNS or SQS, then it needs to have internet access. 
You can consider VPC Endpoints, NAT Gateway or NAT Instances
```

12. The biggest drawback of VPC-enabled functions is that they suffer significantly longer cold starts.
```
Creating and attaching ENIs is time-consuming and can often take up to 10s or more.
Effectively, this makes VPC-enabled functions unsuitable for any user-facing APIs.
```
 
13. Security:
```
With or without VPCs, you should monitor the egress traffic from your functions. Ex: PureSec’s FunctionShield library lets you block outbound internet connectivity, except those destined for other AWS resources.

The EC2 instances that host our Lambda functions are not publicly accessible. It is therefore also not possible for attackers to compromise our functions by compromising the host. 

Unlike EC2 instances, which need VPCs to shield them from malicious traffic. Lambda functions are protected by AWS Identity and Access Management (IAM) service, which provides both authentication and authorization.

All incoming requests have to be signed with a valid AWS credential, and the caller must have the correct IAM permission.

Services such as SNS and DynamoDB are considered secure, even though they don’t run inside a VPC, then why shouldn’t Lambda functions be considered secure when they are protected by the same IAM service?
```
