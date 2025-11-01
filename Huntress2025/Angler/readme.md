## Chall description
```
Category: Misc
These scribbles are impossible to read!

42 6c 6f 77 66 69 73 68

Some crazy fisherman came by, dropped this note, and was muttering something in his drunken stupor, about his fishing pole and taking out... murlocs in Entra? and CyberChef!?
I don't get it. You're the expert here! Not me!
```
## Procedure

We have a file called `scribbles.dat`, with some hex data, after trying to decode with cyberchef we did'nt have any, Is just an encrypted file, the hex data `42 6c 6f 77 66 69 73 68` say something abuout blowfish encryption but nothing about key to decrypt the file, since blowfish need a `KEY` and `IV` to decrypt the file, i decided to use `426c6f7766697368` as KEY and IV, and I was able to decrypt the file and we can see banary.

```bash
echo "426c6f7766697368" | xxd -r -p
Blowfish%
```

<img width="1344" height="633" alt="Screenshot 2025-10-13 at 6 14 17 PM" src="https://github.com/user-attachments/assets/ba0fb262-601a-4d6d-911e-3f39cd4189a4" />

Decoding the binary, we have hex data, but when try to decode the hex data, again nothing

<img width="1341" height="771" alt="Screenshot 2025-10-13 at 6 15 11 PM" src="https://github.com/user-attachments/assets/38faefa9-3210-4ae2-9b9a-f97c0d552061" />

After a while, I decide to try with `magic` on cyberchef, and we can see something like a reversed `base64`

<img width="1347" height="698" alt="Screenshot 2025-10-13 at 6 15 47 PM" src="https://github.com/user-attachments/assets/6dc82bc2-7f3d-4500-85a3-9a110fa7b5ef" />

And finally we were able to decrypt the file, the chall say something like `Entra`, so this could be `Microsoft Entra ID` credentials

<img width="1346" height="869" alt="Screenshot 2025-10-13 at 6 16 17 PM" src="https://github.com/user-attachments/assets/8ce14350-7675-43b6-a36b-17c7b2460f7e" />

After try to login, we have the MFA activated, this is the first problem.

<img width="1444" height="418" alt="Screenshot 2025-10-13 at 6 18 15 PM" src="https://github.com/user-attachments/assets/13cc16f2-89cb-46f7-9122-a1a4c4b13c3d" />

Checking for which available logins options, we can see our first flag\
**Submit the bonus flag that ends with the character `2` below.**

<img width="1094" height="209" alt="Screenshot 2025-10-13 at 6 18 40 PM" src="https://github.com/user-attachments/assets/82f1e882-8638-4a65-8dff-03be8f8b8c41" />

Reading about how can I enter; I found a reference to [az cli](https://learn.microsoft.com/es-es/cli/azure/install-azure-cli?view=azure-cli-latest)
```bash
az help
Group
    az
Subgroups:
    account                 : Manage Azure subscription information.
    acr                     : Manage private registries with Azure Container Registries.
    ad                      : Manage Microsoft Entra ID (formerly known as Azure Active Directory,
                              Azure AD, AAD) entities needed for Azure role-based access control
                              (Azure RBAC) through Microsoft Graph API
...snip...
```

Now we just need to run `az login --allow-no-subscriptions`, this will give us a link and code to use with our Entra ID creds `phisher@4rhdc6.onmicrosoft.com:PhishingAllTheTime19273!!`

<img width="1311" height="62" alt="Screenshot 2025-10-13 at 6 42 57 PM" src="https://github.com/user-attachments/assets/e060455c-e51f-4467-9f91-9dd9d3001fa8" />

<img width="1366" height="452" alt="Screenshot 2025-10-13 at 6 42 31 PM" src="https://github.com/user-attachments/assets/6e0819ad-cbdc-4464-8d04-7045de8ff53f" />

```bash
az login --allow-no-subscriptions
To sign in, use a web browser to open the page https://microsoft.com/devicelogin and enter the code BT9LPDH9J to authenticate.

Retrieving tenants and subscriptions for the selection...
The following tenants don't contain accessible subscriptions. Use `az login --allow-no-subscriptions` to have tenant level access.
05985beb-42bc-4c24-bf49-c1730a825406 'HuntressCTF'

[Tenant and subscription selection]

No     Subscription name          Subscription ID                       Tenant
-----  -------------------------  ------------------------------------  ------------------------------------
[1] *  N/A(tenant level account)  05985beb-42bc-4c24-bf49-c1730a825406  05985beb-42bc-4c24-bf49-c1730a825406

The default is marked with an *; the default tenant is '05985beb-42bc-4c24-bf49-c1730a825406' and subscription is 'N/A(tenant level account)' (05985beb-42bc-4c24-bf49-c1730a825406).

Select a subscription and tenant (Type a number or Enter for no changes): 1

Tenant: 05985beb-42bc-4c24-bf49-c1730a825406
Subscription: N/A(tenant level account) (05985beb-42bc-4c24-bf49-c1730a825406)

[Announcements]
With the new Azure CLI login experience, you can select the subscription you want to use more easily. Learn more about it and its configuration at https://go.microsoft.com/fwlink/?linkid=2271236

If you encounter any problem, please open an issue at https://aka.ms/azclibug

[Warning] The login output has been updated. Please be aware that it no longer displays the full list of available subscriptions by default.
```

We start listing the users with `az ad user list`, I will use `az ad user list -o table` for short output 😅, we have some interething emails, I was trying sending an email for those accounts with msg `test/phisher/blowfish/42 6c 6f 77 66 69 73 68` but nothing.

```bash
DisplayName        GivenName    JobTitle           Mail                               OfficeLocation    PreferredLanguage    Surname    UserPrincipalName
-----------------  -----------  -----------------  ---------------------------------  ----------------  -------------------  ---------  ---------------------------------
Adele Vance        Adele        Retail Manager     AdeleV@4rhdc6.onmicrosoft.com      18/2111           en-US                Vance      AdeleV@4rhdc6.onmicrosoft.com
Diego Siciliani    Diego        HR Manager         DiegoS@4rhdc6.onmicrosoft.com      14/1108           en-US                Siciliani  DiegoS@4rhdc6.onmicrosoft.com
dk.admin                                                                                                                                dk.admin@4rhdc6.onmicrosoft.com
Grady Archie       Grady        Designer           GradyA@4rhdc6.onmicrosoft.com      19/2109           en-US                Archie     GradyA@4rhdc6.onmicrosoft.com
Henrietta Mueller  Henrietta    Developer          HenriettaM@4rhdc6.onmicrosoft.com  18/1106           en-US                Mueller    HenriettaM@4rhdc6.onmicrosoft.com
Isaiah Langer      Isaiah       Sales Rep          IsaiahL@4rhdc6.onmicrosoft.com     20/1101           en-US                Langer     IsaiahL@4rhdc6.onmicrosoft.com
jh.admin                                                                                                                                jh.admin@4rhdc6.onmicrosoft.com
Johanna Lorenz     Johanna      Senior Engineer    JohannaL@4rhdc6.onmicrosoft.com    23/2102           en-US                Lorenz     JohannaL@4rhdc6.onmicrosoft.com
Joni Sherman       Joni         Paralegal          JoniS@4rhdc6.onmicrosoft.com       20/1109           en-US                Sherman    JoniS@4rhdc6.onmicrosoft.com
Lee Gu             Lee          Director           LeeG@4rhdc6.onmicrosoft.com        23/3101           en-US                Gu         LeeG@4rhdc6.onmicrosoft.com
Lidia Holloway     Lidia        Product Manager    LidiaH@4rhdc6.onmicrosoft.com      20/2107           en-US                Holloway   LidiaH@4rhdc6.onmicrosoft.com
Lynne Robbins      Lynne        Planner            LynneR@4rhdc6.onmicrosoft.com      20/1104           en-US                Robbins    LynneR@4rhdc6.onmicrosoft.com
Megan Bowen        Megan        Marketing Manager  MeganB@4rhdc6.onmicrosoft.com      12/1110           en-US                Bowen      MeganB@4rhdc6.onmicrosoft.com
Miriam Graham      Miriam       Director           MiriamG@4rhdc6.onmicrosoft.com     131/2103          en-US                Graham     MiriamG@4rhdc6.onmicrosoft.com
Nestor Wilke       Nestor       Director           NestorW@4rhdc6.onmicrosoft.com     36/2121           en-US                Wilke      NestorW@4rhdc6.onmicrosoft.com
Patti Fernandez    Patti        President          PattiF@4rhdc6.onmicrosoft.com      15/1102           en-US                Fernandez  PattiF@4rhdc6.onmicrosoft.com
Phisher            Phisher      Novice Phisher     phisher@4rhdc6.onmicrosoft.com     131/1104          en-GB                Phisher    phisher@4rhdc6.onmicrosoft.com
Pradeep Gupta      Pradeep      Accountant         PradeepG@4rhdc6.onmicrosoft.com    98/2202           en-US                Gupta      PradeepG@4rhdc6.onmicrosoft.com
ts.admin
```

After listing groups I found my second flag\
**Submit the bonus flag that ends with the character `c` below.**
```
az ad group list -o table
CreatedDateTime       Description                    DisplayName         MailEnabled    MailNickname    RenewedDateTime       SecurityEnabled    SecurityIdentifier
--------------------  -----------------------------  ------------------  -------------  --------------  --------------------  -----------------  ----------------------------------------------------
2025-09-23T22:51:16Z  nattyp@51tjxh.onmicrosoft.com  flag{mczxals2amxc}  False          c8f2dbdc-0      2025-09-23T22:51:16Z  True               S-1-12-1-3020703366-1109955063-3448111285-1491417405
```

Listing app (was a rabbit hole)
```
az ad app list -o table
DisplayName                                                            Id                                    AppId                                 CreatedDateTime
---------------------------------------------------------------------  ------------------------------------  ------------------------------------  --------------------
aad-extensions-app. Do not modify. Used by AAD for storing user data.  7c3a29a8-0473-4d07-8ce0-276b3d7666b8  56100863-e351-4a21-b46d-8791689a47ed  2025-09-23T22:32:55Z
```

Then after listing `sp`, with `--all` option I got two flags\
**Submit the bonus flag that ends with the character `a` below.**\
**Submit the bonus flag that ends with the character `m` below.**
```json
...snip...
  {
    "accountEnabled": true,
    "addIns": [],
    "alternativeNames": [],
    "appDescription": null,
    "appDisplayName": "AAD Request Verification Service - PROD",
    "appId": "c728155f-7b2a-4502-a08b-b8af9b269319",
    "appOwnerOrganizationId": "f8cdef31-a31e-4b4a-93e4-5f571e91255a",
    "appRoleAssignmentRequired": false,
    "appRoles": [],
    "applicationTemplateId": null,
    "createdDateTime": "2023-09-16T06:40:15Z",
    "deletedDateTime": null,
    "description": null,
    "disabledByMicrosoftStatus": null,
    "displayName": "AAD Request Verification Service - PROD",
    "homepage": null,
    "id": "0f125847-7e80-4891-9aa9-9c06b38963fd",
    "info": {
      "logoUrl": null,
      "marketingUrl": null,
      "privacyStatementUrl": null,
      "supportUrl": null,
      "termsOfServiceUrl": null
    },
    "keyCredentials": [],
    "loginUrl": null,
    "logoutUrl": "https://aadrvs.msidentity.com/",
    "notes": "flag{2naxajsmcwijdm}",
    "notificationEmailAddresses": [],
    "oauth2PermissionScopes": [],
    "passwordCredentials": [],

...snip...
{
    "accountEnabled": true,
    "addIns": [],
    "alternativeNames": [],
    "appDescription": null,
    "appDisplayName": "Microsoft Graph Command Line Tools",
    "appId": "14d82eec-204b-4c2f-b7e8-296a70dab67e",
    "appOwnerOrganizationId": "cdc5aeea-15c5-4db6-b079-fcadd2505dc2",
    "appRoleAssignmentRequired": true,
    "appRoles": [],
    "applicationTemplateId": null,
    "createdDateTime": "2025-09-22T22:31:58Z",
    "deletedDateTime": null,
    "description": null,
    "disabledByMicrosoftStatus": null,
    "displayName": "Microsoft Graph Command Line Tools",
    "homepage": "https://docs.microsoft.com/en-us/graph/powershell/get-started",
    "id": "ccc43fab-a89e-480e-ad69-ebecfca74621",
    "info": {
      "logoUrl": null,
      "marketingUrl": null,
      "privacyStatementUrl": "https://privacy.microsoft.com/en-us/privacystatement",
      "supportUrl": null,
      "termsOfServiceUrl": "https://docs.microsoft.com/en-us/legal/microsoft-apis/terms-of-use?context=graph/context"
    },
    "keyCredentials": [],
    "loginUrl": null,
    "logoutUrl": null,
    "notes": "flag{3mcnzxjaslwinca}",
    "notificationEmailAddresses": [],
```

After a while I was able to login on admin tenant, the MFA was not active for this 🤔

I was playing with `purview` audit and filtering the word `flag` with dates `sep-today`, I was able to get `d` flag, just download the `CSV` files when query has finished\
**Submit the bonus flag that ends with the character `d` below.**
<img width="733" height="61" alt="Screenshot 2025-10-13 at 8 13 42 PM" src="https://github.com/user-attachments/assets/48688cdd-af43-4e72-8e16-d5b1d99050b9" />

The last flag was driving me crazy, doing enumeration again, I saw an interesthing email account for `flag{mczxals2amxc}` owner, this is a different domain, that is not in the emails listed before. I decided to sent an email again with Subject and body `flag/phisher/blowfish/42 6c 6f 77 66 69 73 68/426c6f7766697368`, and finally  I got the last flag, 
```
az ad group list -o table
CreatedDateTime       Description                    DisplayName         MailEnabled    MailNickname    RenewedDateTime       SecurityEnabled    SecurityIdentifier
--------------------  -----------------------------  ------------------  -------------  --------------  --------------------  -----------------  ----------------------------------------------------
2025-09-23T22:51:16Z  nattyp@51tjxh.onmicrosoft.com  flag{mczxals2amxc}  False          c8f2dbdc-0      2025-09-23T22:51:16Z  True               S-1-12-1-3020703366-1109955063-3448111285-1491417405
```
#### What is the FINAL flag? This flag is unlike the others and ends with a `?` character.
<img width="1268" height="313" alt="Screenshot 2025-10-13 at 8 29 25 PM" src="https://github.com/user-attachments/assets/75096fc9-3b1e-4ca1-90a1-b426dcff6e9d" />




