## General Notes:

1. AWS Security Token Service (AWS STS) is used to create and provide trusted users with temporary security credentials that can control access to your AWS resources.
2. You can provide access to your AWS resources to users **without having to define an AWS identity for them.**
3. Temporary credentials are the **basis for roles and identity federation.**

### Requesting Temporary Security Credentials

1. AssumeRole—Cross-Account Delegation and Federation Through a Custom Identity Broker
2. AssumeRoleWithWebIdentity—Federation Through a Web-Based Identity Provider
3. AssumeRoleWithSAML—Federation Through an Enterprise Identity Provider Compatible with SAML 2.0
4. GetFederationToken—Federation Through a Custom Identity Broker
5. GetSessionToken—Temporary Credentials for Users in Untrusted Environments

![Compare STS API Options](images/stsapicompare.png)
