## Name: encryptor
#### Category: rev mobile
#### Difficulty: N/A
#### Description: My friend sent me this app with an encoded flag, but he forgot to implement the decryption algorithm! Can you help me out?

## Procedure
We can see an APK file, I will recover the apk code using the site ```http://www.javadecompilers.com/apk```
<br>

## MainActivity.java Content
After recover the source code, we have an interesting code in file ```encryptor.apk/sources/com/example/encryptor/MainActivity.java```
1) The encryptText(String str) method takes a string and encrypts it using the Blowfish algorithm with a key retrieved from the getKey() method.
2) The result of the encryption is Base64-encoded and returned as a string.
3) The encryption key is obtained from the getKey() method, which decodes a Base64 string: "ZW5jcnlwdG9yZW5jcnlwdG9y" (which decodes to "encryptorencryptor").
4) Upon clicking a button that triggers encrypt_onClick(), the user input is encrypted and displayed in a dialog.
5) The getflag_onClick(View view) method reads a file called "enc.txt" from the app's assets and displays it to the user.
   
```
private String getKey() {
        return new String(Base64.decode("ZW5jcnlwdG9yZW5jcnlwdG9y".getBytes(), 0));
    }

private String encryptText(String str) throws InvalidKeyException, UnsupportedEncodingException, NoSuchPaddingException, NoSuchAlgorithmException, IllegalBlockSizeException, BadPaddingException {
        SecretKeySpec secretKeySpec = new SecretKeySpec(getKey().getBytes("UTF-8"), "Blowfish");
        Cipher instance = Cipher.getInstance("Blowfish");
        if (instance != null) {
            instance.init(1, secretKeySpec);
            return Build.VERSION.SDK_INT >= 26 ? new String(Base64.encode(instance.doFinal(str.getBytes("UTF-8")), 0)) : "";
        }
        throw new Error();
    }

public void encrypt_onClick(View view) throws UnsupportedEncodingException, NoSuchPaddingException, IllegalBlockSizeException, NoSuchAlgorithmException, BadPaddingException, InvalidKeyException {
        this.builder.setMessage(encryptText(((TextView) findViewById(R.id.input)).getText().toString())).setCancelable(true);
        AlertDialog create = this.builder.create();
        create.setTitle("Here's your encrypted text:");
        create.show();
        View findViewById = create.findViewById(16908299);
        if (findViewById instanceof TextView) {
            ((TextView) findViewById).setTextIsSelectable(true);
        }
    }

public void getflag_onClick(View view) {
        this.builder.setMessage(readAssetFile(this, "enc.txt")).setCancelable(true);
        AlertDialog create = this.builder.create();
        create.setTitle("Here's the encrypted flag:");
        create.show();
        View findViewById = create.findViewById(16908299);
        if (findViewById instanceof TextView) {
            ((TextView) findViewById).setTextIsSelectable(true);
        }
    }
```

We need to read the ```enc.txt``` file, I have amulated the apk file and click on Get Flag buttom to see the encrypted flag
![Screenshot 2024-09-05 at 11 30 59 AM](https://github.com/user-attachments/assets/648646d5-24b9-4e0c-b32f-0f4a715b7db3)


We have all the parametes we need to decrypt the flag, so i wrote the following python script to recover the flag

```
from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import unpad
import base64

ct = "OIkZTMehxXAvICdQSusoDP6Hn56nDiwfGxt7w/Oia4oxWJE3NVByYnOMbqTuhXKcgg50DmVpudg="
key = b"encryptorencryptor"

encrypted_data = base64.b64decode(ct)
cipher = Blowfish.new(key, Blowfish.MODE_ECB)
flag = unpad(cipher.decrypt(encrypted_data), Blowfish.block_size)
print(flag)

```

output ```CSCTF{3ncrypt0r_15nt_s4Fe_w1th_4n_h4Rdc0d3D_k3y!}```
