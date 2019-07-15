# General Notes

## Compute Services:
1. EC2
2. EC2 Autoscaling
3. Light Sail
4. Lamda
5. ECS

Linux Amazon Machine Images use one of two types of virtualization: paravirtual (PV) or hardware virtual machine (HVM). The main differences between PV and HVM AMIs are the way in which they boot and whether they can take advantage of special hardware extensions (CPU, network, and storage) for better performance. For the best performance, AWS recommends use of current generation instance types and HVM AMIs when you launch your instances. 

**Note:** EC2 makes use of Xen and Nitro Hypervisors.

### HVM: Closest to the Baremetal on AWS.
HVM AMIs are presented with a fully virtualized set of hardware and boot by executing the master boot record of the root block device of your image. This virtualization type provides the ability to run an operating system directly on top of a virtual machine without any modification, as if it were run on the bare-metal hardware. The Amazon EC2 host system emulates some or all of the underlying hardware that is presented to the guest.

## Instance Type:
### Multi-tenant and Dedicated options
	On-Demand Instances:
		On-Demand instances let you pay for compute capacity by the hour or second (minimum of 60 seconds) with no long-term commitments. 
	Spot Instances: Spare capacity in AWS are used for this.
		Bidding
			Analytics and massively parallel computations can be run on Spot Instances as they typically cost 50 to 90% less. 
	Reserved: No Upfront, Full Upfront, Partial Upfront. Upto 75% off on OnDemand instances.
		Standard Reserved Instances - Upto 75% off on OnDemand instances.
		Convertible Reserved Instances - Upto 55% off on OnDemand instances.
		Scheduled Reserved Instances

### Instance Types
	General Purpose
		T2/T3 Burstable Instances - Baseline performance and ability to Burst governed by the CPU credits that are reset every 24 hours. Credits accumulate when utilisation is below the Baseline.
	Compute Optimized
	Memory Optimized
	Storage Optimized
	GPU Optimized - EC2 GPU instances are now called EG instance type.

### Tenancies:
	Dedicated: Dedicated Instances are Amazon EC2 instances that run in a virtual private cloud (VPC) on hardware that's dedicated to a single customer. Dedicated Instances that belong to different AWS accounts are physically isolated at the hardware level. In addition, Dedicated Instances that belong to AWS accounts that are linked to a single payer account are also physically isolated at the hardware level.

	Each instance that you launch into a VPC has a tenancy attribute. This attribute has the following values.
		Default - Your instance runs on shared hardware.
		Dedicated -  Your instance runs on single-tenant hardware.
		Host - Your instance runs on a Dedicated Host, which is an isolated server with configurations that you can control. When this option is chosen you need to choose the Dedicated Host on which this instance needs to be launched.

		After you launch an instance, there are some limitations to changing its tenancy.
			You cannot change the tenancy of an instance from default to dedicated or host after you've launched it.
			You cannot change the tenancy of an instance from dedicated or host to default after you've launched it.
			You can change the tenancy of an instance from dedicated to host, or from host to dedicated after you've launched it.

	If you launch an instance into a VPC that has an instance tenancy of a Dedicated Instance, your instance is automatically a Dedicated Instance, regardless of the tenancy of the instance.

### EC2 Bare Metal - OS runs directly on Physical Hardware i.e no Hypervisor/Virtualization

### EC2 Fleet:
	EC2 fleet enables you to use multiple instance types and purchase models to provision capacity cost effectively across various AZ's. EC2 Fleet is Region scoped and no additional costs for using EC2 Fleet.

	You can create an EC2 Fleet specification defining target capacity, which EC2 instance types work for you, and how much of your fleet should be filled using On-Demand, RI and Spot purchase models. You can also indicate whether EC2 Fleet should take into account the number of cores and amount of memory on each instance or consider all instances equal when scaling. EC2 Fleet then launches the lowest price combination of instances to meet the target capacity based on these preferences.

### EC2 Storage:
	EBS - Data not lost if EC2 Terminates if we set the Storage Delete flag to No. Data is replicated within the AZ so we can restore the data if the disk fails.
	Instance Store - Data lost on Terminate or when Drive fails. Cannot detach and attach to another instance. Because of the short comings they are a little faster than EBS.

### EC2 AutoScaling:
	Launch Configuration - WHAT (AMI, Storage, Keypair etc.. everything related to an EC2 instance config goes here)
	AutoScaling Groups with Scaling Policies to attach to the Launch Configuration - WHERE (AZ's to run the launch config), HOW (ELB load balancing, start size, final size), WHEN (Scaling policy triggers)
	Scaling Policy
		Simple Scaling
		Step Scaling
	General Best practice is to Scale-Up quickly and Scale-Down gradually.
	Warm up period in the ASG section is the time it takes for new EC2 instances to warm-up and until this time expires the instance is not used to serve traffic.
	Autoscaling is not meant to handle instant load spikes and rather mean to scale gradually over a short period of time.
	If we wanted to change the instance type for the instance that are going to be launched in the future:
		Create a new Launch Configuration.
		Replace the existing Launch Configuration attached to the Autoscaling Group.
	Types of Scaling Options supported on Autoscaling Groups:
		Scheduled
		Dynamic
		Manual
	Attach an existing EC2 instance to an Autoscaling Group:
		The instance must be in running state.
		The AMI used to launch the instance must still be available.
		The instance is not a member of another Autoscaling Group.
		The instance is in the same AZ as the Autoscaling Group.
		If the ASG has an attached Target Group or ELB then the ALB/ELB and the Instance must be in the same VPC.
	At this time, Predictive Scaling only generates schedules for EC2 instances.

AWS does not copy launch permissions, user-defined tags, or Amazon S3 bucket permissions from the source AMI to the new AMI.

### EC2 Placement Groups:
	You can launch or start instances in a placement group, which determines how instances are placed on underlying hardware. 

	You cannot move an existing instance to a placement group, move an instance from one placement group to another, or remove an instance from a placement group. Before you begin, the instance must be in the stopped state. You can change the placement group for an instance using the command line or an AWS SDK. 

	EC2 Placement groups do not support tagging. 

	You cant Merge Placement Groups.

	Spread placement groups have a specific limitation that you can only have a maximum of 7 running instances per Availability Zone

	If you start or launch an instance in a partition placement group and there is insufficient unique hardware to fulfill the request, the request fails. Amazon EC2 makes more distinct hardware available over time, so you can try your request again later.

	When you create a placement group, you specify one of the following strategies for the group:
		Cluster – clusters instances into a low-latency group in a single Availability Zone
			A cluster placement group is a logical grouping of instances within a single Availability Zone. A placement group can span peered VPCs in the same Region. The chief benefit of a cluster placement group, in addition to a 10 Gbps flow limit, is the non-blocking, non-oversubscribed, fully bi-sectional nature of the connectivity. In other words, all nodes within the placement group can talk to all other nodes within the placement group at the full line rate of 10 Gbps flows and 25 aggregate without any slowing due to over-subscription.

			Cluster placement groups are recommended for applications that benefit from low network latency, high network throughput, or both, and if the majority of the network traffic is between the instances in the group. 

		Partition – Partition placement groups spread EC2 instances across logical partitions and ensure that instances in different partitions do not share the same underlying hardware, thus containing the impact of hardware failure to a single partition.

			Partition placement groups help reduce the likelihood of correlated hardware failures for your application. When using partition placement groups, Amazon EC2 divides each group into logical segments called partitions. Amazon EC2 ensures each partition within a placement group has its own set of racks, with each rack having its own network and power source. No two partitions within a placement group share the same racks, allowing you to isolate the impact of hardware failure within your application.

		Spread – spreads instances across underlying hardware
			A spread placement group is a group of instances that are each placed on distinct racks, with each rack having its own network and power source.

			A spread placement group can span multiple Availability Zones in the same Region.

Limits - Per region limits
	You are limited to: running up to 20 on-demand instances, purchasing 20 reserved instances, and requesting 5 spot instances per region. 


### General:
	You can redirect internal traffic to a standby instance in case your instance fails, by reassigning the Secondary Private IP address to the standby instance.

	AWS VM Import/Export can be used to bring VMs into AWS. You can also export previously imported VMs.

	Root Disk is where the OS will be installed and it can only be GP2 or SSD. It needs to unencrypted at launch but can be encrypted later.

### Lamda:
	1. Event driven compute service - Run your code in reponse to Events from S3 or DynamoDB etc
	2. Run your code in response to HTTP requests via API gateway or HTTP API calls make from AWS SDK.
	3. There are a whole bunch of Triggers
