## General Notes

1. With AWS Systems Manager Parameter Store, you can create `Secure String` parameters, which are parameters that have a plaintext parameter name and an encrypted parameter value.
2. Parameter Store uses AWS KMS keys to encrypt the parameter values of secure string parameters when you create or change them and to decrypt the parameter values when you access them.
3. You can use the AWS managed key that Parameter Store creates for your account or specify your own customer managed key.
4. Like Secrets Manager: Parameter Store supports only `symmetric KMS keys`. You cannot use an asymmetric KMS key to encrypt your parameters.
5. Parameter Store does not perform any cryptographic operations. Instead, it relies on AWS KMS to encrypt and decrypt secure string parameter values. 


### KMS Differences between SSM Parameter Store and Secrets Manager
1. `SSM Workflow involves no Data keys and rather uses the KMS key directly` - When you create or change a standard secure string parameter value, Parameter Store calls the AWS KMS Encrypt operation. `This operation uses a symmetric encryption KMS key directly to encrypt the parameter value instead of using the KMS key to generate a data key.`
2. You can select the KMS key that Parameter Store uses to encrypt the parameter value. If you do not specify a KMS key, Parameter Store uses the AWS managed key that Systems Manager automatically creates in your account. This KMS key has the `aws/ssm` alias. To view the `aws/ssm` KMS key for your account:
```
aws kms describe-key --key-id alias/aws/ssm
```
3. SSM Secure String (KMS usage) Workflow:
   1. To create a standard secure string parameter, use the PutParameter operation in the Systems Manager API. Include a Type parameter with a value of SecureString. To specify a KMS key, use the KeyId parameter. The default is the AWS managed key for your account, aws/ssm.
   2. Parameter Store then calls the AWS KMS Encrypt operation with the KMS key and the plaintext parameter value. AWS KMS returns the encrypted parameter value, which Parameter Store stores with the parameter name.
   3. Example for SecureString using default `aws/ssm` key `aws ssm put-parameter --name MyParameter --value "secret_value" --type SecureString`
   4. Example for SecureString using CMK `aws ssm put-parameter --name param1 --value "secret" --type SecureString --key-id AAAAAAAA-12BB-12FF-12EE-1234567890ab`