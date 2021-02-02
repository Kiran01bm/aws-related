
## CMKs
1. AWS KMS supports symmetric and asymmetric CMKs. 
2. A Symmetric CMK represents a 256-bit key that is used for Encryption and Decryption. 
3. An Asymmetric CMK represents an RSA key pair that is used for encryption and decryption or signing and verification (but not both), or an elliptic curve (ECC) key pair that is used for signing and verification.
4. By default, AWS KMS creates the key material for a CMK. **You cannot extract, export, view, or manage this key material.**
5. You can import your own key material into a CMK or create the key material for a CMK in the AWS CloudHSM cluster associated with an AWS KMS custom key store.
6. AWS Systems Manager Parameter Store supports only KMS Symmetric CMKs for Encryption of Parameters.

AWS KMS supports three types of CMKs: customer managed CMKs, AWS managed CMKs, and AWS owned CMKs\. 


| Type of CMK | Can view CMK metadata | Can manage CMK | Used only for my AWS account | [Automatic rotation](rotate-keys.md) | 
| --- | --- | --- | --- | --- | 
| [Customer managed CMK](#customer-cmk) | Yes | Yes | Yes | Optional\. Every 365 days \(1 year\)\. | 
| [AWS managed CMK](#aws-managed-cmk) | Yes | No | Yes | Required\. Every 1095 days \(3 years\)\. | 
| [AWS owned CMK](#aws-owned-cmk) | No | No | No | Varies | 


### Operations
| Operation | CMK key type | CMK key usage | 
| --- | --- | --- | 
| [Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) | Any | ENCRYPT\_DECRYPT | 
| [Encrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) | Any | ENCRYPT\_DECRYPT | 
| [GenerateDataKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html) | Symmetric  | ENCRYPT\_DECRYPT | 
| [GenerateDataKeyPair](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyPair.html) | Symmetric \[1\] | ENCRYPT\_DECRYPT | 
| [GenerateDataKeyPairWithoutPlaintext](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyPairWithoutPlaintext.html) | Symmetric \[1\] | ENCRYPT\_DECRYPT | 
| [GenerateDataKeyWithoutPlaintext](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.html) | Symmetric | ENCRYPT\_DECRYPT | 
| [GenerateRandom](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateRandom.html) | N/A\. This operation doesn't use a CMK\. | N/A | 
| [ReEncrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_ReEncrypt.html) | Any | ENCRYPT\_DECRYPT | 
| [Sign](https://docs.aws.amazon.com/kms/latest/APIReference/API_Sign.html) | Asymmetric | SIGN\_VERIFY | 
| [Verify](https://docs.aws.amazon.com/kms/latest/APIReference/API_Verify.html) | Asymmetric | SIGN\_VERIFY | 

\[1\] `GenerateDataKeyPair` and `GenerateDataKeyPairWithoutPlaintext` generate an asymmetric data key pair that is protected by a symmetric CMK\.

## Data Keys
1. Data Keys can be Symmetric or Asymmetric.
2. You can use KMS Symmetric CMKs to generate, encrypt, and decrypt data keys.
3. You cannot use an Asymmetric CMK to generate data keys.
4. AWS KMS does not store, manage, or track your data keys, or perform cryptographic operations with data keys. 
```
You must use and manage data keys outside of AWS KMS.
```
5. **GenerateDataKey**
```
Generates a unique symmetric data key for client-side encryption. 

This operation returns a plaintext copy of the data key and a copy that is encrypted under a customer master key (CMK) that you specify. 

You can use the plaintext key to encrypt your data outside of AWS KMS and store the encrypted data key with the encrypted data.
```
6. **GenerateDataKeyWithoutPlaintext** - To get only an encrypted copy of the data key.
7. **GenerateRandom** - To get a cryptographically secure random byte string.

### Using Data Keys outside of KMS
#### To encrypt data outside of AWS KMS

1. Use the GenerateDataKey operation to get a data key.

2. Use the plaintext data key (in the Plaintext field of the response) to encrypt your data outside of AWS KMS. Then erase the plaintext data key from memory.

3. Store the encrypted data key (in the CiphertextBlob field of the response) with the encrypted data.

#### To decrypt data outside of AWS KMS

1. Use the Decrypt operation to decrypt the encrypted data key. The operation returns a plaintext copy of the data key.

2. Use the plaintext data key to decrypt data outside of AWS KMS, then erase the plaintext data key from memory.


## Data Key Pairs
1. They are designed to be used for client-side encryption and decryption or signing and verification outside of AWS KMS.
2. AWS KMS protects the private key in each data key pair under a Symmetric CMK in AWS KMS that you specify. 
3. AWS KMS does not store, manage, or track your data key pairs, or perform cryptographic operations with data key pairs. 
```
You must use and manage data key pairs outside of AWS KMS.
```
4. AWS KMS supports the following types of data key pairs:
```
RSA key pairs: RSA_2048, RSA_3072, and RSA_4096
Elliptic curve key pairs, ECC_NIST_P256, ECC_NIST_P384, ECC_NIST_P521, and ECC_SECG_P256K1
```
5. **GenerateDataKeyPair** returns a plaintext public key, a plaintext private key, and an encrypted private key.
6. **GenerateDataKeyPairWithoutPlaintext** returns a plaintext public key and an encrypted private key, but not a plaintext private key. 
```
ParameterStore only allows one Version to be active at a time where was Secrets Manager allows more than one version to be active at a time).
```