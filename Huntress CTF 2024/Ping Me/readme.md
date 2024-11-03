## Name: Ping Me
#### Author: @JohnHammond
#### Category: Malware
#### Difficulty: N/D
#### Description: We found this file in the autoruns of a host that seemed to have a lot of network activity... can you figure out what it was doing?

## Procedure
1


````
flag = [102,108,97,103,123,54,100,49,98,54,48,52,98,98,49,98,54,100,97,51,50,98,56,98,98,99,97,57,101,50,54,100,53,49,53,56,57,125,35,35]

out = ""
for x in flag:
  out+=chr(x)

print(out)
````
