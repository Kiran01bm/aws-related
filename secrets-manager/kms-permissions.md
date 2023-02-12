## General Notes

### Permissions for the KMS key
1. When Secrets Manager uses a KMS key in cryptographic operations, it acts on behalf of the user who is accessing or updating the secret value.

2. To retrieve a secret, the user must have `kms:Decrypt` permission granted in either an IAM policy or a key policy.

3. To update the secret, the user must have both `kms:Decrypt` and `kms:GenerateDataKey` permission granted in **either an IAM policy or a key policy.**

4. To allow the KMS key to be used only for requests that originate in Secrets Manager, you can use the kms:ViaService condition key with the secretsmanager.<Region>.amazonaws.com value.

Ref: https://docs.aws.amazon.com/secretsmanager/latest/userguide/security-encryption.html#security-encryption-authz