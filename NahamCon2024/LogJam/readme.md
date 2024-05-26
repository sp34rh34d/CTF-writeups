## Name: LogJam
#### Category: Forensics
#### Difficulty: hard
#### Description: We detected some suspicious activity on one of our endpoints and found this shortcut file in the startup folder. Are you able to figure out what's going on? We've included some log files to help with your analysis. NOTE, Archive password: infected-logjam 

## Procedure
Checking the zip content we can see the following files

````
LogJam
├── Application.evtx
├── Security.evtx
├── System.evtx
└── Updater.lnk
````

Im lazy 😂, i just run ```strings Application.evtx -n 20``` command and got the following output, interesting base64 string<br>

<img width="1676" alt="Screenshot 2024-05-26 at 00 39 16" src="https://github.com/sp34rh34d/CTF-writeups/assets/94752464/1824a72b-37ff-4cbc-9def-83eadd109f11">
<br>

executing the command.
```
echo "JHU3ZkluWSA9ICBbQ2hBcltdXSIpJyduSU9qLV0yLDExLDNbZW1hbi4pJypSZG0qJyBlbEJBaXJhdi1URWcoKCAmIHwpOTNdckFoQ1tdZ05JUlRTWywpMjAxXXJBaENbKzE3XXJBaENbKzY4XXJBaENbKChFY0FMcGVyLiknKSAoRG5FT1RkQUVyLikpaWljc2E6Ol1nTklkb0NOZS5UeEV0Lm1FVFN5Jysnc1sgLCApJysnKVNzRVJwTW9jRUQ6Ol1lRE9NTm9JU1NlcnBNb0MuTm9Jc1NFUnBNT2MuT0kubWV0U1lzJysnWyAsKScrJ2ZHVj04dysySVgyaS8nKycvUHgrRDFMZERkdmdESHgwRGE0cmZTc2lzc1ZEanFaWHJYZCcrJ0h3d2dJTWRkK2IrJysnSTJqM3I0ak5lS1RZRlgrSCsrbW5QNEwwdTNzTnN2SkhtZUFPTEg4OFQwMzBNMGx1aEJ6QklHQ3V3b1pYN3laUmJuYmc3YTE3NFBJVEdjNVhsaXAvRC96NlU1Vlo3bk8vQVBCV3ZJWllOaGRkd0tEc0c4QTc2QTdmTWVmOCcrJ082dk1mbmNnQycrJ2k5Z0hIZlF2anhxK3k4SmliZCtGK1RkZ3F0SzRIQ09WalpnNzgvNlJSaGpnMUEwWUg0SkllZmQvRUxrb2hsRG81R1Vkd0tmaXVaSURORlNmc3I4RXM5Wi9UMmd5eWZZNUs1OW1aMFdGLzFtbDU4cHNPMU12YmZXTnhvTmhwbURIeWFuMDVBbTJ5NFhRbS8vaVNFRlZmSFpFL09mOGpQZ3ZFUElmSitad21MR05lVkNVQjNoTUtjNW43Y1A3MTNrelJ4L2EzOVdTVllCL2VCcWxjZGsyUU9RVTMwL1BEZHA5WWkzVTNRUmg4d2crZVp1L1QyWGNqdEEnKyczR1pRM0FWUVRwTzZacjJrdkNSZ0tnVlRyTjdQQU5aZS9SREJjK1Y4JysnRWpKWmdLQ0VUVDdwRnBnV3ptYUN4cndxODJEWFNOTlovRlJaTScrJ3FEaUNxMkJ1bGFRZGJvV0FvYScrJ0gnKyduMEVVOVVENlFockZPUVJ1dTF5aHIzbFRSUGNyNXNqWTQyOG4zcy90NTY1NE8vaUZPcnZnZWdKVVFGS2ZaN1J1WUFRUjFCUFJhaC9Ua3B3ZFF3UDdaJysnRDVIUTNyRScrJ0d4JysnL0tBWk5HSEFVOUtDSkJpZ2xHWUxraXExeFRGL2lMWHUwK2tDeWJlSGFodDJ1L3N5cTB6S2plTW41dk9JYnZ5KzZtcnQ3LzhxbFRjbTEnKycyQ0sxdG9tbk5BYitjWDZzbHBkYTJjbS90a0ZaZlZhalAvUUdCYWxTaEwrbzh1ZS9UQkRpRDlhK05reC9WMjZPN2NqVTVaeCs5SFcyJysnaWUzeScrJ0ZTaVhLNkM4VHRLeGsnKydUNEU5Zk1VJysnS0pnSU5SaDMydVdWcicrJ0pYJysnTGh5aTJQQUlrUUpDaU4xV1VFcUFGZS91bGpVOEpQcjRKYklxZkRpZ1NkWlJDbENVQ2ZwSENyaFVaWScrJzRoeTRFU25qVkF0aWZCVVRiL2NnamRRbXUvaldpbitCMldiNTQnKydQTUhnOE95cycrJ3F2KycrJy9YYnNuJysnNjdIaTVFM0hjR2JUNzhmdHBMaEFodVdRN0kwZUNWZzVwR053VnNKZWlEZWpIL3ZYZEtoVVVkSmNLYkxhL1l4OG1NRlJxVzVXcDFRaHpzelUyWGxVcU03bnBaVkd6c3NtNTViNGMyQjVJQicrJ1FSWlhuT2lFenYvcjVpblF1bEkzV2FGTDBpWCcrJ0lqMkpRN2N4T1MxUFhkTE9FVmlPSXFLWW85M0FYSUQ4UFErMlBFNCcrJ3MnKyc5YnBSVmZmR1YgKEcnKydOJysnSScrJ1J0czQ2ZXNhJysnQk1PckY6Ol1UcmV2Tm9DW11NQUVSVHNZck9tZU0uT2knKycubWVUc3lzWyhtQUVydHNlVEFMRmVkLm5PJysnSVNzRXJQbU9jLm9pLm1FVFN5JysncyAgdGNFakJPLXdlTiAoIChSRWRBZXJNYWVSdFMub2kubWVUc3knKydTICB0Y0VqQk8td2VOICggbk9Jc3NFUnBYRS1lS09WTmknKCI7IFthclJhWV06OnJldmVyU2UoICggIFZBcklBQmxlICgnVTcnKydmSU5ZJykgLXZBKSApOy4oICRWZXJiT1NlcHJFZkVSZW5jRS50T1NUUmluZygpWzEsM10rJ3gnLUpvaU4nJykoIC1Kb0lOKCAgVkFySUFCbGUgKCdVNycrJ2ZJTlknKSAtdkEpICkgCg==" | base64 -d
``` 

I got the following output, save the output as a txt file<br>

``` 
$u7fInY =  [ChAr[]]")''nIOj-]2,11,3[eman.)'*Rdm*' elBAirav-TEg(( & |)93]rAhC[]gNIRTS[,)201]rAhC[+17]rAhC[+68]rAhC[((EcALper.)') (DnEOTdAEr.))iicsa::]gNIdoCNe.TxEt.mETSy'+'s[ , )'+')SsERpMocED::]eDOMNoISSerpMoC.NoIsSERpMOc.OI.metSYs'+'[ ,)'+'fGV=8w+2IX2i/'+'/Px+D1LdDdvgDHx0Da4rfSsissVDjqZXrXd'+'HwwgIMdd+b+'+'I2j3r4jNeKTYFX+H++mnP4L0u3sNsvJHmeAOLH88T030M0luhBzBIGCuwoZX7yZRbnbg7a174PITGc5Xlip/D/z6U5VZ7nO/APBWvIZYNhddwKDsG8A76A7fMef8'+'O6vMfncgC'+'i9gHHfQvjxq+y8Jibd+F+TdgqtK4HCOVjZg78/6RRhjg1A0YH4JIefd/ELkohlDo5GUdwKfiuZIDNFSfsr8Es9Z/T2gyyfY5K59mZ0WF/1ml58psO1MvbfWNxoNhpmDHyan05Am2y4XQm//iSEFVfHZE/Of8jPgvEPIfJ+ZwmLGNeVCUB3hMKc5n7cP713kzRx/a39WSVYB/eBqlcdk2QOQU30/PDdp9Yi3U3QRh8wg+eZu/T2XcjtA'+'3GZQ3AVQTpO6Zr2kvCRgKgVTrN7PANZe/RDBc+V8'+'EjJZgKCETT7pFpgWzmaCxrwq82DXSNNZ/FRZM'+'qDiCq2BulaQdboWAoa'+'H'+'n0EU9UD6QhrFOQRuu1yhr3lTRPcr5sjY428n3s/t5654O/iFOrvgegJUQFKfZ7RuYAQR1BPRah/TkpwdQwP7Z'+'D5HQ3rE'+'Gx'+'/KAZNGHAU9KCJBiglGYLkiq1xTF/iLXu0+kCybeHaht2u/syq0zKjeMn5vOIbvy+6mrt7/8qlTcm1'+'2CK1tomnNAb+cX6slpda2cm/tkFZfVajP/QGBalShL+o8ue/TBDiD9a+Nkx/V26O7cjU5Zx+9HW2'+'ie3y'+'FSiXK6C8TtKxk'+'T4E9fMU'+'KJgINRh32uWVr'+'JX'+'Lhyi2PAIkQJCiN1WUEqAFe/uljU8JPr4JbIqfDigSdZRClCUCfpHCrhUZY'+'4hy4ESnjVAtifBUTb/cgjdQmu/jWin+B2Wb54'+'PMHg8Oys'+'qv+'+'/Xbsn'+'67Hi5E3HcGbT78ftpLhAhuWQ7I0eCVg5pGNwVsJeiDejH/vXdKhUUdJcKbLa/Yx8mMFRqW5Wp1QhzszU2XlUqM7npZVGzssm55b4c2B5IB'+'QRZXnOiEzv/r5inQulI3WaFL0iX'+'Ij2JQ7cxOS1PXdLOEViOIqKYo93AXID8PQ+2PE4'+'s'+'9bpRVffGV (G'+'N'+'I'+'Rts46esa'+'BMOrF::]TrevNoC[]MAERTsYrOmeM.Oi'+'.meTsys[(mAErtseTALFed.nO'+'ISsErPmOc.oi.mETSy'+'s  tcEjBO-weN ( (REdAerMaeRtS.oi.meTsy'+'S  tcEjBO-weN ( nOIssERpXE-eKOVNi'("; [arRaY]::reverSe( (  VArIABle ('U7'+'fINY') -vA) );.( $VerbOSeprEfERencE.tOSTRing()[1,3]+'x'-JoiN'')( -JoIN(  VArIABle ('U7'+'fINY') -vA) )
```
<br>

This is an encoded powershell command, thanks to my friend **Bravosec**, i use PowerDecode tool to deobfuscate the malicious code, you can download PowerDecode from ```https://github.com/Malandrone/PowerDecode```
<br>

Start the PowerDecode.bat file, and select the txt file with the malicious code<br>
<img width="1659" alt="Screenshot 2024-05-26 at 00 57 16" src="https://github.com/sp34rh34d/CTF-writeups/assets/94752464/adead5ce-676d-4269-af29-390beb3e7f8a">
<br>

We can see a base64 string as last layer, just run ```echo "ZmxhZ3tjYThjMjg4ZDEzOTU2ODk1NzcyODdiYTNiZjI2NDlhZH0=" | base64 -d ```<br>

<img width="442" alt="Screenshot 2024-05-26 at 00 57 24" src="https://github.com/sp34rh34d/CTF-writeups/assets/94752464/b832b718-acdd-4151-823b-e1b9d36b6247">
<br>

flag ```flag{ca8c288d1395689577287ba3bf2649ad}```


