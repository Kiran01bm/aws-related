# General Notes

## S3:
	Size of s3 bucket is unlimited Theoritically.
	Bucket Name must be globally unique
	Bucket can be used to host Static Website
	Bucket Website Re-direction feature
	Cross-Region Replication - Charges Apply
	Transfer Acceleration - Charges Apply - Makes use of CloudFront Edge Locations internally. Users to Edge over Internet and Edge to S3 over AWS's backbone network.
		Use Amazons Transfer Acceleration Test Site.
	S3 Bucket names must be Globally Unique irrespective of the region they are in.
	Life Cycle Policies
	Supports Server side encryption and has features to support Client side encryption
	1st Byte latency is in milliseconds for all Storage Classes except for Glacier.
	By Default a Bucket is private and wont be accessible Publicly.
	We can apply an Objecy Lock to prevent an Object from being deleted.
	3 Factors:
		Security
		Durability
		Availability
		Latency
	Every Bucket has:
		Name
		Bucket Access Policy
	Every Object has:
		Key
		Value
		VersionID
		Metadata
		ACLs
	Based on Eventual Consistency
		New Objects - Read After Write Consistency - PUT
		Update and Deletes - Eventual Consistency - PUT and DELETE
	Security
		IAM Policies
		Bucket Policies - Applied at the Bucket Level
		ACL Policies - Applied at Bucket and Object level
		Supports Encryption at Rest and in Transit.
			Transit - Is with HTTPS
			Rest:
				Server Side
					S3 Managed Keys - SSE-S3 - Server Side Encryption S3
					KMS Key - SSE-KMS - Server Side Encryption with KMS managed keys
					Customer Provided Keys - SSE-C - Server Side Encryption with Customer Provided Keys
				Client Side - Done by user or a client library such as Amazon S3 Encryption Client
				The valid ways of encrypting data on S3 are Server Side Encryption (SSE)-S3, SSE-C, SSE-KMS or a client library such as Amazon S3 Encryption Client. 
		Access logging on a bucket can be enabled and the logs can be sent to another bucket or another bucket in another account.
	
	Durability - 11 9's Durability across the 6 S3 storage classes
	
	Availability of Standard and Standard IA - 99.99 as its 3 AZ replication amazon guarantee is 99.9. Standard One Zone IA - 99.5
	
	Versioning:
		Once enabled it cannot be disabled but it can be suspended
		Great backup tool
		Integrates with Lifecycle rules
		MFA Delete - Delete a object

	Tiered Storage:
		Standard
		Standard IA - Lower fee than S3 but there is Retrieval Fee
		Standard IA - 1 zone - Really Low Cost Option. Object is literally stored in one AZ
		Standard Intelligent Tiering - This has automation to move objects between Standard and Standard IA.
		Reduced Redundancy Storage on S3 
			- Reduced Redundancy Storage (RRS) is an Amazon S3 storage option that enables customers to store noncritical, reproducible data at lower levels of redundancy than Amazon S3’s standard storage.
			- The only s3 storage class with 99.99% Durability. It also has 99.99 availability
			- Can only tolerage 1 AZ failure, Where as Standard and IA can tolerate 2 AZ failures as the content is replicated ans stored in >= 3 AZs 

	LifeCycle Management: Can be applied to both Current and Previous Versions
		Transitions 
			- Automate the Transition to lower cost Storage Classes
		Expirations
			- Remove the objects
		We can even remove incomplete multi-part uploads.

	Replication:
		We can enable cross region replication at bucket level of based on search patterns and wild cards.
		Can be replicated to Buckets within the Account or to Buckets into another Account.
		If your bucket as 10 objects and 100 versions and you enable cross region replication the old objects and versions wont be replicated.
		If you delete an object then the Delete Markers are not replicated and also Individual version deletes are not replicated - This is intentional by AWS to prevent propogation of accidental deletes.

	Partitions are based on Key Prefix - Hence to increase Performance use multiple Key Prefix
	S3 Versioning
		Deleted Objects can be restored
		Objects can be restored to Previous versions
	Server-side encryption encrypts only the object data. Any object metadata is not encrypted. 
	http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingServerSideEncryption.html

	https://docs.aws.amazon.com/AmazonS3/latest/dev/ShareObjectPreSignedURL.html

	With a single PUT operation, you can upload objects up to 5 GB in size. Using the multipart upload API, you can upload large objects, up to 5 TB. File size can be anywhere between 0 and 5TB.
		https://docs.aws.amazon.com/AmazonS3/latest/dev/UploadingObjects.html

	Reduced Redundancy Storage(RRS) is an Amazon S3 storage option that enables customers to reduce their costs by storing noncritical, reproducible data at lower levels of redundancy that Amazon S3's standard storage. It provides a cost effective, highly available solution for distributing or sharing content that is durably stored elsewhere, or for storing thumbnails, transcoded media, or the processed data that can be easily reproduced. The RRS option stores objects on multiple devices across multiple facilities, providing 400 times the durability of a typical disk drive, but does not replicate objects as many times as a standard Amazon S3 storage.

	You increase S3 performance by:
		Add a hash string as prefix to the key name,
	  	Add more prefixes in your key name, or
	  	Reverse the key name string.

	You must explicitly enable versioning on your bucket. By default, versioning is disabled. Regardless of whether you have enabled versioning, each object in your bucket has a version ID.

	You can also enable MFA on delete from S3.

	Amazon S3 can send event notifications when objects are uploaded to Amazon S3. Amazon S3 event notifications can be delivered using Amazon SQS or Amazon SNS, or sent directly to AWS Lambda, enabling you to trigger workflows, alerts, or other processing.

	Whether you're storing multimedia files such as photos and videos or pharmaceutical files, or financial data Amazon S3 can be used as your big data object store.

	Static Website on S3: Sample URL
		http://BUCKETNAME.s3-website-us-east-1.amazonaws.com/ReadMe.txt

## Glacier
	Durability - 11 9s across 3 AZs
	Restoration from Glacier to S3 takes 3 to 5 hours (RTO)
	Only supports Server Side encryption
	Using AWS export we cannot directly export data from Glacier we should use S3 lifecycle restore to get content into S3 from Glacier and then we can export data from s3 using AWS export.
	We can also use AWS import to get data into EBS, S3 and Glacier.
	Glacier Tiers:
		S3 Glacier - Retrieval time configurable from Minutes to Hours.
		S3 Glacier Deep Archive - Lowest cost Storage class on S3 and Retrieval Time 12 hours or more.

## Service Pairs:
	S3, Glacier
	EBS, EFS
	Storage Gateway (Can work on top of AWS Direct Connect to Provide a Low latency link connecting On-Prem DC to S3) and Snow Ball

## EFS:
	Create EFS Fileshare and Mount Targets per subnet to access the EFS fileshare from an EC2 instance within the Subnet.
	NAS File Storage
	RWX from clients
	Fully Managed Service
	Multi AZ Replication and Data is spread across AZs
	Can scale to Petabytes scale and support thousands of concurrent NFS connections
	Since mount targets are within a Subnet all the Subnet security features are available like ACL's
	Security in terms of Security Groups too.
	Can Encrypt at Rest and in Transit
	Encrypt in Transit is enabled by adding "-o tls" in the mount command "sudo mount -t efs -o tls fs-abcdfe:/ mountdir"
	EFS supports NFSv4 protocol
	Read After Write Consistency.
	EFS also has Life Cycle Management and Infrequent Access Storage

## EBS Volumes:
	EBS volumes are by default replicated within the AZ. There are 2 copies within an AZ.

	EBS Options:
		SSD - GP2, Provisioned IOPS
		Magnetic

	EBS snapshots are point in time and incremental and backups are stored in S3.

	EBS encryption is at Rest and Intransit between the EC2 instance and EBS volume.

	To check if the block device has a Filesystem on it (and to get the UUID) ex: file -s /dev/xvdb

	Volume Sizes:
		Maximum volume sizie with any option is 16TiB
		Min volume size, IOPS
			GP2 - 1GiB, 16,000
			IO1 - 4GiB, 64,000
			st1 - 500GiB, 500
			sc1 - 500GiB, 250

	Changing Volumes Storage Class and Expanding Size can be done Online or Live or On-The-Fly.

	Migrate EC2 from One AZ to Another AZ:
		Create Snapshot
		Create Image/AMI from the Snapshot
		Use the Image/AMI above to Create a EC2 instance
		or
		Create a AMI from the volume
		Use the AMI to create an EC2 instance.

	Migrate EC2 from One Region to Another Region:
		Create Snapshot
		Create Image/AMI from the Snapshot
		Copy Image/AMI to the Desired Region	
		or
		Create a AMI from the volume
		Copy Image/AMI to the Desired Region

	Any EBS Volumes attached to an EC2 instance wont be deleted by Default when the EC2 instance is terminated.
	By Default, Both EBS backed and Instance store root volumes will be deleted when instance terminates however we can change EBS not to be deleted.

	AMI/Images can be created from both Volumes and Snapshots.
		Volume --> Snapshot --> AMI
		Volume --> AMI	

	EBS vs Instance Stores:
		AMIs Root Volume can be backed by either EBS or Instance Store. For EBS - EBS Volume is created from a EBS Snapshot stored in S3. For Instance Store - Volume is created from a template stored in S3.
		
		The data in an instance store persists only during the lifetime of its associated instance. If an instance reboots (intentionally or unintentionally), data in the instance store persists. However, data in the instance store is lost under the following circumstances: The underlying disk drive fails or host fails, The instance stops, The instance terminates.

		We can add EBS volumes after the Instance is Operational but Instance store can only be added before start.

		EC2 instances based on Instance Store can only be Terminated or Rebooted.

	Encrypting EBS Volumes:
		Unecrypted Volume --> Snapshot --> COPY Snapshot enable Encryption (Encrypted Snap) --> Create AMI (Encrypted AMI) --> Launch EC2 from Encrypted AMI.
		Snapshots of Encrypted volumes are Encrypted automatically.
		Volumes restored from Encrypted snapshots are Encrypted automatically.

	Snapshots can be shared with the Public or Other AWS accounts as long as they are UnEncrypted.

	You can add multiple volumes to an EC2 instance and then create your own RAID 5/RAID 10/RAID 0 configurations using those volumes to increase the IOPS

## Storage Gateway:
	Customers side Storage Gateway Appliance and behind this you may have your application server
	AWS Side Storage Gateway Backend and behind this you will have s3, EBS and Glacier
	Both the above ones connected via Direct Connect or over the Internet
	Virtual Appliance on a VM on client side (stateless app so can be scaled out) or a Hardware Appliance on client side.

	File Gateway:
		Interface to s3 with file protocols like NFS
		Objects can be directly accessed in S3
		10 Fileshares per File Gateway
		5tb max file size
	Volume Gateway:
		iSCSI access to s3
		Access in AWS through EBS snapshots to create new EBS volumes
		32 volumes per volume gateway
		Cached Mode - 32TB max volume size and 1PB per volume gateway
		Stored Mode - 16TB max volume size and 512gb per volume gateway
		You can also do snapshots of those volumes
	Tape Gateway:
		iSCSI VTL - Virtual Tape Library access to s3
		Data can be archived to Glacier
		A single tape gateway can have up to 1500 virtual tapes in the VTL with a maximum aggregate capacity of 1 PB
		With a tape gateway, you can cost-effectively and durably archive backup data in Amazon Glacier.

	By using cached volumes, you can use Amazon S3 as your primary data storage, while retaining frequently accessed data locally in your storage gateway. Cached volumes minimize the need to scale your on-premises storage infrastructure, while still providing your applications with low-latency access to their frequently accessed data.

	Gateway-Stored volumes store your primary data locally, while asynchronously backing up that data to AWS. Depending on the Cache allocated you can achieve the same with File Gateway
