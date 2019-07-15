# General Notes:

## Networking Services and Content Delivery:
1. Coudfront - Caching, DDoS protection
	You can define TTL for the assets and when TTL expires CloudFront distribution resyncs the content from Origin ex: S3 bucket
	You can invalidate the entire cloudfront distribution with a /* or invalidate specific content by specifying the path to the document ex: /assets/hourly/12.html
	You can even set-up http https redirection
	You can also terminate traffic at the CloudFront distribution

2. VPC - Can span multiple AZs within a Region

3. Direct Connect - Physical High Speed Fiber Optic Private connection between your Enterprise and AWS

4. ELB - HA and Fault-tolerance. Can be used to Distribute traffic between multiple EC2 instances across AZ's

5. Route53 - Amazon Route 53 Traffic Flow makes it easy for you to manage traffic globally through a variety of routing types

6. API Gateway - Help deploy secure API services. Its a server less service

## Route53:
	If you purchase a Domain via AWS then a Hosted Zone will be automatically created after the Domain Purchase process is completed.

	DNS Propogation can be checked with - https://www.whatsmydns.net

	There is a limit of 50 domain names which can be increased by contacting AWS

	Hosted Zone Types:
		Private Hosted Zones
		Public Hosted Zones

	Traffic Flow Polcies

	Routing Policies:
		Simple Routing (Routing to a Single Resource all others handle routing to multiple backend resources)
		Failover Routing - All of the below Routing Flow options can be combined with DNS Failover
			2 A records and you designate one as Primary and the other as Secondary and each record will have its associated Healthcheck
			Active-Passive - Route traffic from a unhealthy instance to a static site ex: Route traffic from Webserver to a Static site on S3
		Weighted Round Robin Routing
			Multiple A records for each domain name with weight assigned to each record + Healthcheck can be assigned to each record.
		MultiValue Answer Routing
			Same as Simple record set but allows you to set Healthchecks on each record set.
		Latency Routing
			Multiple A records and the records will have Latency as the Routing Policy and each record will associate the Region with its Back End be it EC2 or ELB resource.
		Geo-Location Routing
			Multiple A records with Geo Location set as the routing policy - Associate each A record with a Continent or Country.
			If a DNS query originates from India then the A record associated with India will be returned to the user.
		Geo-Proximity Routing
			Must have an associated Traffic flow policy.
			Lets route traffic your resources based on the location of your users and your resources.

	Alias Records 
		- Are same as CNAME but one difference. Alias records can be created for the Zone Apex and can create Alias for all record types except NS and SOA.
		- Alias Records provides a Route53 specific extension to DNS functionality
	CNAME Records 
		- The domain name that you want to resolve to instead of the value in the Name field.
		- CNAME cannot be created for the Zone Apex	


	Route 53 Weighted Round Robin can be used for managing risk with production application updates by releasing updates using staged increases in the percentage of users receiving the updates.

	Amazon Route 53 health checks integrate with CloudWatch metrics so you can do the following:

	  Verify that a health check is properly configured.
	  Review the health of a health check endpoint over a specified period of time.
	  Configure CloudWatch to send an Amazon Simple Notification Service (Amazon SNS) alert when Amazon Route 53 considers your specified endpoint to be unhealthy.

	Route53 Health Checks:
		Can be used to conduct healthchecks and make decissions based on health.
		Healthchecks can be set on individual record sets ex: Server1, Server2, Server3 - Each can be serving under example.com and has separate records each associated with a health check and weight associated to each record.
		If a Healthcheck fails then the Record Set will be removed from Route53 until the healthchecks pass.
		You can send SNS notifications for failed Health Checks


## ELB:
	With ELB sticky sessions if the Instance becomes unhealthy the request is routed to another healthy instance.
		2 types: Once ELB managed and another is Application Managed
			1. Duration Based - Where ELB adds a Header named AWSELB if no cookie is present and route the traffic to an instance with least load. This header then gets used subsequently for stickiness.	
			2. Application Based - Application generates the cookie in response and ELB inserts a stickiness cookie.

	Proxy Protocol support in ELB allows Client IP and Client Protocol to be added as a custom header and sent to the backend apps and back end apps needs to have the Proxy Protocol capability to be able to read these headers and do the needful.

	While creating an ELB you never specify an IP address. After ELB creation we get to know the DNS name and AWS managed the IP and the service behind it.

	Connection Draining allows ELB to retain the connection to an unhealthy backend for a configurable period (between 1 sec to 3600sec) to allow inflight requests to drain completely.

	With Enhanced Monitoring ELB sends metrics to CloudWatch every 60 seconds (as opposed to the free tier where metrics are sent every 5 minutes)

	Each ELB node produces log file at 5 to 60 min intervals which is saved to S3.

	ELB can spread load across AZs not regions.

	The load balancer cannot distribute traffic across Regions but can distribute traffic across Domains.

	When Cross Zone load balancing is enabled every ELB node can route traffic to back end nodes in different AZ.

	When creating and ELB the AZs that you select is the AZs in which the ELB nodes will be deployed by AWS.

	ServerOrder preferance lists the ciphers that the Server Prioritises.. ie the server picks the 1st cipher in its list that is supported by the client.

	AWS Certificate manager integrates very well with ELB and certificates are issued free of cost.

	Controller Service is an ELB component which is responsible for monitoring the Load Balancers.

	The X-Forwarded-For request header helps you identify the IP address of a client when you use HTTP/HTTPS load balancer. Because load balancers intercept traffic between clients and servers, your server access logs contain only the IP address of the load balancer. Elastic Load Balancing stores the IP address of the client in the X-Forwarded-For request header and passes the header along to your server.

	To create an ELB you need atleast 2 Public Subnets

## Target Group: Target Groups link ELB to the Backend. ALB or NLB needs Target Group but CLB routes traffic back to EC2 instances directly.
	Backends can be:
		EC2 Instance
		External IP - ELB can be used to Load Balance requests to systems outside of AWS
		Lamda

## Classic Load Balancer:
	Layer 4 and Layer 7. Layer 7 support is limited Ex: It does not support websockets.
	Does not need target group.
	Cheaper in cost and lesser features.
	Classic LB routes requests to backends with least load.
	Sticky Sessions can be enabled to route traffic to a specific ec2 isntance.

## Application Load Balancer:
	Layer 7 - HTTP, HTTPS, HTTP/2, Websockets etc
	Load balancer deletion protection.
	Supports Path based routing and Sticky Sessions.
	Multi Conatiner load balancing i.e Instance:Port backend
	Target in a Target Group can be an EC2 instance, Conatiner or IP Address (not public IP though)
	Listeners will use Rules to direct traffic to the Target groups
	Does SSL offloading
	Needs Target Group
	Sitcky sessions can be enabled to route traffic to a specific target group i.e not to a specific ec2 instance.
	Cross Zone Load balancing

## Network Load Balancer: 
        Highest performance of the lot for the Load Balancers
	Layer 4. Supports websockets.
	Load Balancer deletion protection.
	Cannot do backend server encryption.
	Cannot do Cross Zone load balancing

	Use Case: Create TargetGroup and use that as Traffic Input for AutoScaling Group and then create a NLB with backend as the Target Group created earlier. So, basically the Target Group is a link between NLB and AutoScaling group.

## VPC:
	When account is created - A Default VPC is created in each of the regions and a Default subnet in each Availability zones.

	5 addresses in total - 1st 4 Addresses and the Last Address in the Subnet is reserved by AWS

	VPC Minimum size supported is /28
	
	VPC Maximum size supported is /16

	You cannot change the size of a VPC once deployed. But can add additional CIDR blocks.
	
	One accounts us-east-1a might refer to AZ1 and another accounts us-east-1a refers to AZ2. 
	
	Internet Gateway - One per VPC

	VPC peering and VPN are connectivity services and cannot control traffic for security.
	
	VPN Gateway - One per VPC and is on the AWS side that needs to be complimented by a VPN Gateway on the customers side. VPN Tunnel between the two gateways.
	
	### Security:
		1. VPC Flow Logs - Capture in Cloudwatch logs. For Audit and can be used for Intelligent decission making
		2. Subnet ACLs - Subnet level, Evaluates rules in the Order so if there is a deny it drops the packets and wont continue with the rest of the rules. If there are multiple ACLs it applies the Most Restrictive Deny Rule. 1st Layer od Defence for Inbound Traffic.
		3. Security Groups - Instance level, If there are more than one matching rule in SG it applies the Most Permissive Rule. 1st layer of Defence. Evaluates all rules. If there is a deny and permit it permits the traffic. 1st Layer of Defence for Outbound Traffic.

	### Security Groups:
		All InBound traffic is blocked by Default.
		Default security group rules allow all outbound traffic from an instance.
		You cannot have DENY rules. Only ALLOW rules are allowed.
		You can associated multiple security groups to an EC2 instance.

	By default, any user-created VPC subnet WILL NOT automatically assign Public IPv4 Addresses to instances – the only subnet that does this is the “Default” VPC subnets which are automatically created by AWS
	
	Internet Gateway is a Scalable, Redundant and Highly Available VPC Component. Only one Internet gateway can be attached to a VPC at time. It performs NAT for Instances that have been assigned Public IP addresses.

	You can associate secondary IPv4 CIDR blocks with your VPC. When you associate a CIDR block with your VPC, a route is automatically added to your VPC route tables to enable routing within the VPC

	When you use the wizard in the console to create a VPC with a gateway, the wizard automatically updates the route tables to use the gateway. If you’re using the command line tools or the API to set up your VPC, then you have to update the route tables yourself.

	### Limits:
		Default number of VPCs per region is 5. This limit can be increased upon request. 	
		Default number of subnets per VPC is 200. This limit can be increased upon request. 
		Default number of Internet gateways per region is 5 and you can create as many internet gateways as your VPCs per region limit.
		With regards to VPC, The default maximum number of virtual private gateways allowed per region - 5

	### VPC Peering:
		Can Peer across regions
		Can Peer between VPCs in different accounts and in the same account
		Peering is NOT Transitive but a Star configuration
		VPC peering only routes traffic between source and destination VPCs. VPC peering does not support edge to edge routing. 

	When a New VPC is created the following resources are created:
		VPC
		Route Table
		ACL
		SG

	The following cannot Span an AZ:
		Subnet
		NAT Gateway
			Through Put from 5gbps to 45gbps
			Create one NAT gateway per AZ
			NAT Gateways must be deployed in public subnets.

	### One To One Associations:
		VPC and Internetgateway association
		VPC and SG association
		Subnet is part of a VPC and hence inherently One to One
		Subnets to ACL
		Subnet and RouteTable association

	### ACL:
		Default ACL - By default allows all Inbound and Outbound 
		Custom ACL - By default blocks all Inbound and Outbound
		Can Block IP addresses with ACLs and this cant be done with SGs as SGs do not support DENY rules.

	### Flow Logs can be created in the following levels:
		1. VPC
		2. Subnet
		3. NIC/ENI level

		2 Options to send Flow Logs - Can be sent to Cloudwatch and S3
		You can apply filters to the VPC flow logs - You can log Accepts, Rejects or Both

	### VPC Endpoints:
		In contrast to a NAT gateway, traffic between your VPC and the other service does not leave the Amazon network when using VPC endpoints.
		2 Types:
			1. VPC Interface Endpoints - Its an ENI with a Private IP which acts as an entry point to the traffic destined to the supported AWS services (a huge list). Attach an ENI to an EC2 Instance.
			2. VPC Gateway Endpoints - Like NAT gateways and they are supported for S3 and DynamoDB

	### VPN Gateway:
		The VPC has an attached virtual private gateway, and your remote network includes a customer gateway, which you must configure to enable the Site-to-Site VPN connection. You set up the routing so that any traffic from the VPC bound for your network is routed to the virtual private gateway.

		When you create multiple Site-to-Site VPN connections to a single VPC, you can configure a second customer gateway to create a redundant connection to the same external location. You can also use it to create Site-to-Site VPN connections to multiple geographic locations.

		An Amazon VPC VPN connection links your data center (or network) to your Amazon VPC virtual private cloud (VPC). A customer gateway is the anchor on your side of that connection. It can be a physical or software appliance. The anchor on the AWS side of the VPN connection is called a virtual private gateway.

		The following diagram shows your network, the customer gateway, the VPN connection that goes to the virtual private gateway, and the VPC. There are two lines between the customer gateway and virtual private gateway because the VPN connection consists of two tunnels to provide increased availability for the Amazon VPC service. If there's a device failure within AWS, your VPN connection automatically fails over to the second tunnel so that your access isn't interrupted. From time to time, AWS also performs routine maintenance on the virtual private gateway, which may briefly disable one of the two tunnels of your VPN connection. Your VPN connection automatically fails over to the second tunnel while this maintenance is performed. When you configure your customer gateway, it's therefore important that you configure both tunnels.


		"Customer Gateway" and "Virtual Private Gateway". When connecting a VPN between AWS and a third party site, the Customer Gateway is created within AWS, but it contains information about the third party site e.g. the external IP address and type of routing. The Virtual Private Gateway has the information regarding the AWS side of the VPN and connects a specified VPC to the VPN.

		When you create a VPN connection, the VPN tunnel comes up when traffic is generated from your side of the VPN connection. The virtual private gateway is not the initiator; your customer gateway initiates the tunnels.

		The traffic from VPC gateway must be able to leave the VPC and tarverse over the internet to reach the Customer Gateway. Hence Customer Gateway must be assigned a Static IP Address that can be routable via the internet.

		VPC should have an internet gateway attached to it. That way, you can establish a site-to-site VPN with the on-premise environment.

## CloudFront:
	Is not regional its a Global Service
	Origin can be a:
		 S3 bucket
		 EC2 Instance HTTP server
		 ELB
		 Route53
	Can be used to deliver the following Content Types:
		Static
		Dynamic
		Streaming
		Interactive
	Types:
		Web Distribution
		RTMP Distribution - For Media Streaming
	You can also put a WAF policy infront of Cloudfront
	Edge locations are not ReadOnly they can be written into ex: Transfer Acceleration
	Invalidation of Cache is chargeable
	CloudFront must have access to the Origin Server
	Distribution - Is backed by the Origin Server
	Caches GET, HEAD and OPTIONS. GET? (GET with query parameters) POST, PUT and DELETE are proxied to the Origin server
	CloudFront Edge Location
	CloudFront Distribution
	Amazon CloudFront can handle 10,000 requests per second

## API Gateway:
	Backend can be 
		Lamda
		EC2
		DynamoDB
	API Gateway has caching capability responses 
	Is Serverless
	Throttle - 10,000 RPS limit and Burst os 5000requests

## Elastic Network Interface:
        Is part of a Subnet which is part of a VPC and has a SG associated with it. This can be attached to the Elastic IP.
	ENI is AZ Scoped - It is associated with a Subnet which is inside a AZ which is inside a VPC and has a SG associated with it. 
	EIP is VPC Scoped - It has PublicIP, PrivateIP (from a subnet), VPCId, PublicDNS, Attached to an EC2 instance, Attached to a NetworkInterface which can be a ENI

How is the Public IP address managed in an instance session via the instance GUI/RDP or Terminal/SSH session?
	http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html
	The Public IP address is not managed on the instance: It is, instead, an alias applied as a network address translation of the Private IP address.

The instance which has the Oldest Launch Config will terminate 1st
	http://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/AutoScaling
