## Chall description
```
Category: Forensic

Have you ever done forensics on the Recycle Bin? It's... a bit of a mess. Looks like the threat actor pulled some tricks to hide data here though.
The metadata might not be what it should be. Can you find a flag?
```
## Procedure

Extract the `trashcan.zip` file, this contains the following TXT.

```bash
ls
$I01XCGF.txt	$ICVE4M2.txt	$IOSGXAZ.txt	$R08ZI07.txt	$RJUUXYN.txt
$I08ZI07.txt	$ID557GC.txt	$IOXKN7X.txt	$R198LLE.txt	$RK9LJEF.txt
$I0AP14L.txt	$IDEBQ1M.txt	$IOYHHQ5.txt	$R1D6OCR.txt	$RKQ5M0F.txt
$I17RAD1.txt	$IDWR2DY.txt	$IPD4HRC.txt	$R1MMUNX.txt	$RLD51DG.txt
$I198LLE.txt	$IE0RMKA.txt	$IPDV01V.txt	$R2J48PI.txt	$RLN2HDS.txt
$I1D6OCR.txt	$IEFXDY8.txt	$IPMSABA.txt	$R2ZP91D.txt	$RLRXLH5.txt
$I1MMUNX.txt	$IEXEX7I.txt	$IPWI3VK.txt	$R3B7EP8.txt	$RM7QAYI.txt
$I1WD5RF.txt	$IEYL8JP.txt	$IQ6XS48.txt	$R3O4FNO.txt	$RMZ20SR.txt
$I2CVFM2.txt	$IFRUSE0.txt	$IQ9QLU0.txt	$R3Y2C18.txt	$RN4C62C.txt
$I2FNXOW.txt	$IFUV73N.txt	$IQPFIEQ.txt	$R467CFX.txt	$RND6VW0.txt
$I2J48PI.txt	$IG64RJD.txt	$IQQAA2F.txt	$R4S3J0O.txt	$RNG16RB.txt
$I2ZP91D.txt	$IG8TC80.txt	$IR2JCOS.txt	$R4VJ9VP.txt	$ROFYR05.txt
$I3B7EP8.txt	$IGUW5S7.txt	$IS4YB00.txt	$R59AMQZ.txt	$ROSGXAZ.txt
$I3O4FNO.txt	$IHE2HRX.txt	$IS67SUB.txt	$R5F20WX.txt	$ROXKN7X.txt
$I3Y2C18.txt	$IHRXQ2Y.txt	$ISBYUOH.txt	$R5HCDNO.txt	$RPD4HRC.txt
$I467CFX.txt	$IIENSHP.txt	$ISTAZD1.txt	$R5RPN3M.txt	$RPMSABA.txt
$I4S3J0O.txt	$IIIY075.txt	$ISXWEK6.txt	$R60PUB8.txt	$RPWI3VK.txt
$I4VAGUQ.txt	$IISFJJQ.txt	$ITB15DJ.txt	$R61YGX7.txt	$RQ6XS48.txt
$I4VJ9VP.txt	$IIYLT3Z.txt	$ITE5TYG.txt	$R65140O.txt	$RS4YB00.txt
$I59AMQZ.txt	$IJ9U0RR.txt	$ITMVJR4.txt	$R6676MD.txt	$RSBYUOH.txt
$I5F20WX.txt	$IJUUXYN.txt	$ITUQ7CQ.txt	$R7QCZXB.txt	$RSXWEK6.txt
$I5HCDNO.txt	$IJWBEUE.txt	$IU5E39M.txt	$R7UPDZU.txt	$RTB15DJ.txt
$I5RPN3M.txt	$IK9LJEF.txt	$IUDDG43.txt	$R8Q6O5D.txt	$RTE5TYG.txt
$I60PUB8.txt	$IKK9TWO.txt	$IUG82GT.txt	$R90UOKS.txt	$RTUQ7CQ.txt
$I61YGX7.txt	$IKQ5M0F.txt	$IUIEHU7.txt	$RA88SVT.txt	$RU5E39M.txt
$I65140O.txt	$IL2QDPK.txt	$IUQNBS2.txt	$RC04FJS.txt	$RUDDG43.txt
$I6676MD.txt	$IL4WLXW.txt	$IUSDLBT.txt	$RCVE4M2.txt	$RUG82GT.txt
$I7MXUTD.txt	$ILD51DG.txt	$IUYP5MU.txt	$RD557GC.txt	$RUQNBS2.txt
$I7QCZXB.txt	$ILN2HDS.txt	$IV05A2U.txt	$RDEBQ1M.txt	$RUSDLBT.txt
$I7UPDZU.txt	$ILRXLH5.txt	$IV6X20I.txt	$RDWR2DY.txt	$RUYP5MU.txt
$I8Q6O5D.txt	$IM7QAYI.txt	$IW14HF1.txt	$RE0RMKA.txt	$RV6X20I.txt
$I90UOKS.txt	$IMU3AKY.txt	$IW1WPZX.txt	$REXEX7I.txt	$RW14HF1.txt
$I99VSUL.txt	$IMZ20SR.txt	$IWKOHFD.txt	$RG8TC80.txt	$RW1WPZX.txt
$I9PGBL6.txt	$IN4C62C.txt	$IWS5CL5.txt	$RGUW5S7.txt	$RWKOHFD.txt
$IA88SVT.txt	$IND6VW0.txt	$IXEGH08.txt	$RHRXQ2Y.txt	$RWS5CL5.txt
$IABA5GX.txt	$ING16RB.txt	$IXWYRKV.txt	$RIENSHP.txt	$RXEGH08.txt
$IAKHV8Y.txt	$INU5TNU.txt	$IYQJIUH.txt	$RIIY075.txt	$RXWYRKV.txt
$IAZPA8T.txt	$IO7IO01.txt	$IZ3RIQE.txt	$RISFJJQ.txt	$RYQJIUH.txt
$IC04FJS.txt	$IOFYR05.txt	$IZ9EJJK.txt	$RIYLT3Z.txt	$RZ3RIQE.txt
```

**What the Recycle Bin Does Behind the Scenes**

When a file is deleted through the recycle bin on a computer with the NTFS file system, several things will occur. First the NTFS $MFT entry is updated with a new record number for a parent. 
Basically, that means its parent now becomes the Recycle Bin instead of its original location. Next, the file is given a new name. Instead of the original name it now becomes named $R with six 
random characters and the original file extension. For example if a file was named “dog.txt” it could become “$R24E32E.txt”. In addition, a paired administrative file is created. 
This administrative file starts with $I and then has the same six random characters and the original extension. So, the paired administrative file using the example above “$R24E32E.txt” would be “$I24E32E.txt”. 
These $I files contain a good deal of information, even when the paired $R file is overwritten.

The $I files contain:
* The original file’s size
* The date the file was sent to the recycle bin
* The original file’s full path

We can use the tool [$I parser](https://www.flashbackdata.com/downloads/ifileparser.zip) to recover info from Admistrative files `$I` into a CSV file.

<img width="1180" height="242" alt="Screenshot 2025-10-11 at 10 53 30 AM" src="https://github.com/user-attachments/assets/aad27739-1510-4b09-bbcf-7c5d19fab232" />

```csv
"$I File Name","$R File Name","Size (Bytes)","Timestamp (UTC)","Original File Name With Path","Original File Name","MD5 Hash"
"$I01XCGF.txt","$R01XCGF.txt","49","12-14-1642 08:40:03 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","72ccbd51593cb6d2c1b2a5b1b5d025af"
"$I08ZI07.txt","$R08ZI07.txt","50","12-14-1642 08:40:04 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","ec706d437eed73bbd601f839da406614"
"$I0AP14L.txt","$R0AP14L.txt","100","12-14-1642 08:40:11 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","0c5610f24ad2fa0b8fd86e1f6905352c"
"$I17RAD1.txt","$R17RAD1.txt","53","12-14-1642 08:40:01 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","bc7567fdf14b2a67c390ec02af38f659"
"$I198LLE.txt","$R198LLE.txt","101","12-14-1642 08:40:00 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","b3864457646b2f3b70379c71ac08a9a8"
"$I1D6OCR.txt","$R1D6OCR.txt","108","12-14-1642 08:39:41 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","5d6ea5b4b5ab17965ff3c5df15ef260e"
"$I1MMUNX.txt","$R1MMUNX.txt","103","12-14-1642 08:39:43 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","e676dea95705535d0d515dd2abf29252"
"$I1WD5RF.txt","$R1WD5RF.txt","100","12-14-1642 08:39:57 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","9376fe5538aef701842f6e125964a9f1"
"$I2CVFM2.txt","$R2CVFM2.txt","56","12-14-1642 08:40:02 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","7de512d181f9f3e0597c210898885021"
"$I2FNXOW.txt","$R2FNXOW.txt","48","12-14-1642 08:40:10 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","f098d60853e181b75720037023fcf906"
"$I2J48PI.txt","$R2J48PI.txt","98","12-14-1642 08:39:50 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","8da7f328f3939e8d84187d9fa3b190a1"
"$I2ZP91D.txt","$R2ZP91D.txt","50","12-14-1642 08:39:49 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","95d28931b9e67cf2e39604c0d40d6c63"
"$I3B7EP8.txt","$R3B7EP8.txt","56","12-14-1642 08:40:08 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","c56bf62d7e2d7761b1be6be30f16295a"
"$I3O4FNO.txt","$R3O4FNO.txt","54","12-14-1642 08:39:53 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","bd4a8aa7d113c4c91ae31052bac3eb6d"
"$I3Y2C18.txt","$R3Y2C18.txt","108","12-14-1642 08:39:41 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","5d6ea5b4b5ab17965ff3c5df15ef260e"
"$I467CFX.txt","$R467CFX.txt","100","12-14-1642 08:40:11 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","0c5610f24ad2fa0b8fd86e1f6905352c"
"$I4S3J0O.txt","$R4S3J0O.txt","55","12-14-1642 08:39:54 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","7cfaa86d910729f253a289e2f4562896"
"$I4VAGUQ.txt","$R4VAGUQ.txt","125","12-14-1642 08:40:17 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","5caa439e471a3f43c792d833c3748b8f"
"$I4VJ9VP.txt","$R4VJ9VP.txt","50","12-14-1642 08:39:47 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","d89adc3b18caab36f8952cba64555f6f"
"$I59AMQZ.txt","$R59AMQZ.txt","50","12-14-1642 08:39:47 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","d89adc3b18caab36f8952cba64555f6f"
"$I5F20WX.txt","$R5F20WX.txt","48","12-14-1642 08:39:51 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","ce41832bfa2d4c255b8c3de1de9a9290"
"$I5HCDNO.txt","$R5HCDNO.txt","48","12-14-1642 08:40:10 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","f098d60853e181b75720037023fcf906"
"$I5RPN3M.txt","$R5RPN3M.txt","51","12-14-1642 08:40:14 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","f1d301fb7f7bbfa6f234c89563b3e961"
"$I60PUB8.txt","$R60PUB8.txt","101","12-14-1642 08:40:13 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","bd5acfea3801be1abf4b2b9d69e848ba"
"$I61YGX7.txt","$R61YGX7.txt","55","12-14-1642 08:40:06 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","c9eebe932164e324dd9a8f08a34624be"
"$I65140O.txt","$R65140O.txt","57","12-14-1642 08:40:16 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","6162fa4a6bd70f3f0967986a8ead00f4"
"$I6676MD.txt","$R6676MD.txt","53","12-14-1642 08:40:01 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","bc7567fdf14b2a67c390ec02af38f659"
"$I7MXUTD.txt","$R7MXUTD.txt","53","12-14-1642 08:40:12 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","82e91cde2be6988ce9b9e6c999407f94"
"$I7QCZXB.txt","$R7QCZXB.txt","55","12-14-1642 08:39:54 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","7cfaa86d910729f253a289e2f4562896"
"$I7UPDZU.txt","$R7UPDZU.txt","49","12-14-1642 08:40:03 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","72ccbd51593cb6d2c1b2a5b1b5d025af"
"$I8Q6O5D.txt","$R8Q6O5D.txt","97","12-14-1642 08:39:42 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","dcbf5da95032e98424b14ef83c645706"
"$I90UOKS.txt","$R90UOKS.txt","49","12-14-1642 08:39:58 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","00ce9b1f3dedf2548e13d20d7c0ed167"
"$I99VSUL.txt","$R99VSUL.txt","51","12-14-1642 08:40:14 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","f1d301fb7f7bbfa6f234c89563b3e961"
"$I9PGBL6.txt","$R9PGBL6.txt","48","12-14-1642 08:39:51 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","ce41832bfa2d4c255b8c3de1de9a9290"
"$IA88SVT.txt","$RA88SVT.txt","98","12-14-1642 08:39:50 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","8da7f328f3939e8d84187d9fa3b190a1"
"$IABA5GX.txt","$RABA5GX.txt","57","12-14-1642 08:40:16 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","6162fa4a6bd70f3f0967986a8ead00f4"
"$IAKHV8Y.txt","$RAKHV8Y.txt","56","12-14-1642 08:40:08 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","c56bf62d7e2d7761b1be6be30f16295a"
"$IAZPA8T.txt","$RAZPA8T.txt","49","12-14-1642 08:39:58 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","00ce9b1f3dedf2548e13d20d7c0ed167"
"$IC04FJS.txt","$RC04FJS.txt","123","12-14-1642 08:39:44 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","ce871141e53d5eb131cb8ca1663552ac"
"$ICVE4M2.txt","$RCVE4M2.txt","101","12-14-1642 08:39:56 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","5929c9fec7dea3ffeec1c0d27ac87d98"
"$ID557GC.txt","$RD557GC.txt","49","12-14-1642 08:39:55 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","28193872d0b6ae1811671b1215274f29"
"$IDEBQ1M.txt","$RDEBQ1M.txt","48","12-14-1642 08:39:51 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","ce41832bfa2d4c255b8c3de1de9a9290"
"$IDWR2DY.txt","$RDWR2DY.txt","48","12-14-1642 08:40:10 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","f098d60853e181b75720037023fcf906"
"$IE0RMKA.txt","$RE0RMKA.txt","53","12-14-1642 08:40:01 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","bc7567fdf14b2a67c390ec02af38f659"
"$IEFXDY8.txt","$REFXDY8.txt","108","12-14-1642 08:39:41 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","5d6ea5b4b5ab17965ff3c5df15ef260e"
"$IEXEX7I.txt","$REXEX7I.txt","101","12-14-1642 08:40:13 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","bd5acfea3801be1abf4b2b9d69e848ba"
"$IEYL8JP.txt","$REYL8JP.txt","98","12-14-1642 08:39:48 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","b194e35002beacef32feb525638e0a49"
"$IFRUSE0.txt","$RFRUSE0.txt","56","12-14-1642 08:40:07 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","4e391781330bdf8a6c61b2cc485de123"
"$IFUV73N.txt","$RFUV73N.txt","54","12-14-1642 08:40:05 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","b66bafe543a91770fbd056a2cd4b08b7"
"$IG64RJD.txt","$RG64RJD.txt","55","12-14-1642 08:39:54 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","7cfaa86d910729f253a289e2f4562896"
"$IG8TC80.txt","$RG8TC80.txt","100","12-14-1642 08:39:57 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","9376fe5538aef701842f6e125964a9f1"
"$IGUW5S7.txt","$RGUW5S7.txt","101","12-14-1642 08:40:00 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","b3864457646b2f3b70379c71ac08a9a8"
"$IHE2HRX.txt","$RHE2HRX.txt","101","12-14-1642 08:39:56 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","5929c9fec7dea3ffeec1c0d27ac87d98"
"$IHRXQ2Y.txt","$RHRXQ2Y.txt","57","12-14-1642 08:40:16 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","6162fa4a6bd70f3f0967986a8ead00f4"
"$IIENSHP.txt","$RIENSHP.txt","103","12-14-1642 08:39:43 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","e676dea95705535d0d515dd2abf29252"
"$IIIY075.txt","$RIIY075.txt","56","12-14-1642 08:40:07 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","4e391781330bdf8a6c61b2cc485de123"
"$IISFJJQ.txt","$RISFJJQ.txt","97","12-14-1642 08:39:42 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","dcbf5da95032e98424b14ef83c645706"
"$IIYLT3Z.txt","$RIYLT3Z.txt","98","12-14-1642 08:39:48 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","b194e35002beacef32feb525638e0a49"
"$IJ9U0RR.txt","$RJ9U0RR.txt","103","12-14-1642 08:39:43 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","e676dea95705535d0d515dd2abf29252"
"$IJUUXYN.txt","$RJUUXYN.txt","101","12-14-1642 08:39:56 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","5929c9fec7dea3ffeec1c0d27ac87d98"
"$IJWBEUE.txt","$RJWBEUE.txt","123","12-14-1642 08:39:44 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","ce871141e53d5eb131cb8ca1663552ac"
"$IK9LJEF.txt","$RK9LJEF.txt","101","12-14-1642 08:39:59 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","40263b7b88510d6e73cf7374bf54701a"
"$IKK9TWO.txt","$RKK9TWO.txt","53","12-14-1642 08:40:09 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","8578e77bfea7b36633f4bebd611071d2"
"$IKQ5M0F.txt","$RKQ5M0F.txt","53","12-14-1642 08:40:12 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","82e91cde2be6988ce9b9e6c999407f94"
"$IL2QDPK.txt","$RL2QDPK.txt","55","12-14-1642 08:40:06 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","c9eebe932164e324dd9a8f08a34624be"
"$IL4WLXW.txt","$RL4WLXW.txt","50","12-14-1642 08:40:04 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","ec706d437eed73bbd601f839da406614"
"$ILD51DG.txt","$RLD51DG.txt","54","12-14-1642 08:40:05 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","b66bafe543a91770fbd056a2cd4b08b7"
"$ILN2HDS.txt","$RLN2HDS.txt","51","12-14-1642 08:40:14 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","f1d301fb7f7bbfa6f234c89563b3e961"
"$ILRXLH5.txt","$RLRXLH5.txt","56","12-14-1642 08:40:07 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","4e391781330bdf8a6c61b2cc485de123"
"$IM7QAYI.txt","$RM7QAYI.txt","49","12-14-1642 08:39:45 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","31387bdfee91e9eff1ee4f18cfdf87d6"
"$IMU3AKY.txt","$RMU3AKY.txt","97","12-14-1642 08:39:42 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","dcbf5da95032e98424b14ef83c645706"
"$IMZ20SR.txt","$RMZ20SR.txt","101","12-14-1642 08:39:59 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","40263b7b88510d6e73cf7374bf54701a"
"$IN4C62C.txt","$RN4C62C.txt","125","12-14-1642 08:40:17 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","5caa439e471a3f43c792d833c3748b8f"
"$IND6VW0.txt","$RND6VW0.txt","100","12-14-1642 08:40:11 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","0c5610f24ad2fa0b8fd86e1f6905352c"
"$ING16RB.txt","$RNG16RB.txt","50","12-14-1642 08:40:15 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","942b3c3c112a0478eed82e7df1bdcb68"
"$INU5TNU.txt","$RNU5TNU.txt","49","12-14-1642 08:39:45 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","31387bdfee91e9eff1ee4f18cfdf87d6"
"$IO7IO01.txt","$RO7IO01.txt","10","12-14-1642 08:40:18 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","6bba3a63f35b4da87e428f3705c19170"
"$IOFYR05.txt","$ROFYR05.txt","56","12-14-1642 08:40:02 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","7de512d181f9f3e0597c210898885021"
"$IOSGXAZ.txt","$ROSGXAZ.txt","53","12-14-1642 08:39:52 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","731c868cbc3e3dd1c22e09646dde3134"
"$IOXKN7X.txt","$ROXKN7X.txt","56","12-14-1642 08:40:08 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","c56bf62d7e2d7761b1be6be30f16295a"
"$IOYHHQ5.txt","$ROYHHQ5.txt","50","12-14-1642 08:39:49 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","95d28931b9e67cf2e39604c0d40d6c63"
"$IPD4HRC.txt","$RPD4HRC.txt","49","12-14-1642 08:39:45 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","31387bdfee91e9eff1ee4f18cfdf87d6"
"$IPDV01V.txt","$RPDV01V.txt","101","12-14-1642 08:39:59 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","40263b7b88510d6e73cf7374bf54701a"
"$IPMSABA.txt","$RPMSABA.txt","49","12-14-1642 08:39:55 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","28193872d0b6ae1811671b1215274f29"
"$IPWI3VK.txt","$RPWI3VK.txt","50","12-14-1642 08:39:49 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","95d28931b9e67cf2e39604c0d40d6c63"
"$IQ6XS48.txt","$RQ6XS48.txt","49","12-14-1642 08:39:58 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","00ce9b1f3dedf2548e13d20d7c0ed167"
"$IQ9QLU0.txt","$RQ9QLU0.txt","50","12-14-1642 08:40:15 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","942b3c3c112a0478eed82e7df1bdcb68"
"$IQPFIEQ.txt","$RQPFIEQ.txt","53","12-14-1642 08:39:52 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","731c868cbc3e3dd1c22e09646dde3134"
"$IQQAA2F.txt","$RQQAA2F.txt","100","12-14-1642 08:39:46 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","32e10bc4ab91d5768eef846ca60b5c93"
"$IR2JCOS.txt","$RR2JCOS.txt","50","12-14-1642 08:39:47 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","d89adc3b18caab36f8952cba64555f6f"
"$IS4YB00.txt","$RS4YB00.txt","10","12-14-1642 08:40:18 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","6bba3a63f35b4da87e428f3705c19170"
"$IS67SUB.txt","$RS67SUB.txt","49","12-14-1642 08:39:55 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","28193872d0b6ae1811671b1215274f29"
"$ISBYUOH.txt","$RSBYUOH.txt","53","12-14-1642 08:40:12 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","82e91cde2be6988ce9b9e6c999407f94"
"$ISTAZD1.txt","$RSTAZD1.txt","101","12-14-1642 08:40:13 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","bd5acfea3801be1abf4b2b9d69e848ba"
"$ISXWEK6.txt","$RSXWEK6.txt","54","12-14-1642 08:39:53 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","bd4a8aa7d113c4c91ae31052bac3eb6d"
"$ITB15DJ.txt","$RTB15DJ.txt","125","12-14-1642 08:40:17 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","5caa439e471a3f43c792d833c3748b8f"
"$ITE5TYG.txt","$RTE5TYG.txt","102","12-14-1642 08:39:40 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","788a382f169b949abec4bc674a419f3d"
"$ITMVJR4.txt","$RTMVJR4.txt","102","12-14-1642 08:39:40 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","788a382f169b949abec4bc674a419f3d"
"$ITUQ7CQ.txt","$RTUQ7CQ.txt","98","12-14-1642 08:39:48 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","b194e35002beacef32feb525638e0a49"
"$IU5E39M.txt","$RU5E39M.txt","123","12-14-1642 08:39:44 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","ce871141e53d5eb131cb8ca1663552ac"
"$IUDDG43.txt","$RUDDG43.txt","53","12-14-1642 08:40:09 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","8578e77bfea7b36633f4bebd611071d2"
"$IUG82GT.txt","$RUG82GT.txt","10","12-14-1642 08:40:18 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","6bba3a63f35b4da87e428f3705c19170"
"$IUIEHU7.txt","$RUIEHU7.txt","98","12-14-1642 08:39:50 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","8da7f328f3939e8d84187d9fa3b190a1"
"$IUQNBS2.txt","$RUQNBS2.txt","53","12-14-1642 08:40:09 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","8578e77bfea7b36633f4bebd611071d2"
"$IUSDLBT.txt","$RUSDLBT.txt","100","12-14-1642 08:39:46 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","32e10bc4ab91d5768eef846ca60b5c93"
"$IUYP5MU.txt","$RUYP5MU.txt","54","12-14-1642 08:40:05 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","b66bafe543a91770fbd056a2cd4b08b7"
"$IV05A2U.txt","$RV05A2U.txt","101","12-14-1642 08:40:00 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","b3864457646b2f3b70379c71ac08a9a8"
"$IV6X20I.txt","$RV6X20I.txt","49","12-14-1642 08:40:03 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","72ccbd51593cb6d2c1b2a5b1b5d025af"
"$IW14HF1.txt","$RW14HF1.txt","100","12-14-1642 08:39:57 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","9376fe5538aef701842f6e125964a9f1"
"$IW1WPZX.txt","$RW1WPZX.txt","102","12-14-1642 08:39:40 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","788a382f169b949abec4bc674a419f3d"
"$IWKOHFD.txt","$RWKOHFD.txt","56","12-14-1642 08:40:02 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","7de512d181f9f3e0597c210898885021"
"$IWS5CL5.txt","$RWS5CL5.txt","50","12-14-1642 08:40:04 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","ec706d437eed73bbd601f839da406614"
"$IXEGH08.txt","$RXEGH08.txt","100","12-14-1642 08:39:46 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","32e10bc4ab91d5768eef846ca60b5c93"
"$IXWYRKV.txt","$RXWYRKV.txt","50","12-14-1642 08:40:15 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","942b3c3c112a0478eed82e7df1bdcb68"
"$IYQJIUH.txt","$RYQJIUH.txt","53","12-14-1642 08:39:52 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","731c868cbc3e3dd1c22e09646dde3134"
"$IZ3RIQE.txt","$RZ3RIQE.txt","55","12-14-1642 08:40:06 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","c9eebe932164e324dd9a8f08a34624be"
"$IZ9EJJK.txt","$RZ9EJJK.txt","54","12-14-1642 08:39:53 UTC","C:\Users\flag\Desktop\flag.txt","flag.txt","bd4a8aa7d113c4c91ae31052bac3eb6d"
```

Checking the `Timestamp` column, We can see this is not ordered, just order by `A-Z` (I have used excel 👀), We see an interesting data into `bytes` column, let's extract those bytes and convert to char.

```python
flag = [102,102,102,108,108,108,97,97,97,103,103,103,123,123,123,49,49,49,100,100,100,50,50,50,98,98,98,50,50,50,98,98,98,48,48,48,53,53,53,54,54,54,55,55,55,49,49,49,101,101,101,100,100,100,49,49,49,101,101,101,101,101,101,53,53,53,56,56,56,49,49,49,50,50,50,54,54,54,55,55,55,56,56,56,56,56,56,53,53,53,48,48,48,100,100,100,53,53,53,101,101,101,51,51,51,50,50,50,57,57,57,125,125,125,10,10,10]

out = []
for x in flag:
    out.append(chr(x))
print(''.join(out))

### Output
# ffflllaaaggg{{{111ddd222bbb222bbb000555666777111eeeddd111eeeeee555888111222666777888888555000ddd555eee333222999}}}
```

Every byte is repeated 3 times, just delete those repeated bytes.
```python
flag = [102,102,102,108,108,108,97,97,97,103,103,103,123,123,123,49,49,49,100,100,100,50,50,50,98,98,98,50,50,50,98,98,98,48,48,48,53,53,53,54,54,54,55,55,55,49,49,49,101,101,101,100,100,100,49,49,49,101,101,101,101,101,101,53,53,53,56,56,56,49,49,49,50,50,50,54,54,54,55,55,55,56,56,56,56,56,56,53,53,53,48,48,48,100,100,100,53,53,53,101,101,101,51,51,51,50,50,50,57,57,57,125,125,125,10,10,10]

out = []
for x in range(1,len(flag),3):
    out.append(chr(flag[x]))

print(''.join(out))

#flag{1d2b2b05671ed1ee5812678850d5e329}
```

Flag `flag{1d2b2b05671ed1ee5812678850d5e329}`
