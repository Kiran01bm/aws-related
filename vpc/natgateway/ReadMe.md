## NAT Gateway Redundancy/HA/FT

1. A NAT Gateway is **redundant within a single AZ**. The real reason for using multiple NAT Gateways is for high-availability.

2. If there is a single NAT Gateway and that AZ should fail, then all private instances would lose Internet access. Having a NAT Gateway in each AZ ensures high availability.

3. If you are not too concerned about a potentially rare occurrence, you can save money by using only one NAT Gateway. The performance penalty for traffic going between AZs is minor (single-digit millisecond latency).

4. One NAT gateway per AZ could also be more cost effective (depending on the use case): "There will be data transfer charge between your NAT Gateway and EC2 instance if they are in the different availability zone"
