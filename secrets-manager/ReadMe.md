## General Notes

Secrets Manager uses **envelope encryption with AWS KMS keys and data keys to protect each secret value**. 

1. Whenever the secret value in a secret changes, Secrets Manager generates a new data key to protect it. Secrets Manager supports only `symmetric encryption KMS keys` i.e `data keys` used by Secrets Manager are symmetric.
   
2. The data key is encrypted under a KMS key and stored in the metadata of the secret. To decrypt the secret, Secrets Manager first decrypts the encrypted data key using the KMS key in AWS KMS.
   
3. Secrets Manager does not use the KMS key to encrypt the secret value directly. `Instead, it uses the KMS key to generate and encrypt a 256-bit Advanced Encryption Standard (AES) symmetric data key, and uses the data key to encrypt the secret value.` 
   
4. Secrets Manager uses the plaintext data key to encrypt the secret value outside of AWS KMS, and then removes it from memory. It stores the encrypted copy of the data key in the metadata of the secret.
   
5. When you create a secret, you can choose any symmetric encryption customer managed key in the AWS account and Region, `or` you can use the AWS managed key for Secrets Manager (aws/secretsmanager). In the console, if you choose the default value for the encryption key, Secrets Manager creates the AWS managed key aws/secretsmanager, if it doesn't already exist, and associates it with the secret. You can use the same KMS key or different KMS keys for each secret in your account.
   
6. You can change the encryption key for a secret in the console or in the AWS CLI or an AWS SDK with UpdateSecret. When you change the encryption key, Secrets Manager re-encrypts versions of the secret that have the staging labels AWSCURRENT, AWSPENDING, and AWSPREVIOUS under the new encryption key. When the secret value changes, Secrets Manager also encrypts it under the new key. You can use the old key or the new one to decrypt the secret when you retrieve it.

7. To find the KMS key associated with a secret, view the secret in the console or call ListSecrets or DescribeSecret. When the secret is associated with the AWS managed key for Secrets Manager (aws/secretsmanager), these operations do not return a KMS key identifier.