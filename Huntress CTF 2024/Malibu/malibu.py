import requests, base64


buckets_name = """0z5PxaxHEZGdHlUj
1wrJQ2xn/er1UMoYK/aiSEiiU5/DIe2t3yyX3zOeiuA
1wrJQ2xn/mXSo4cTro5ox2B86
2GzIfHPD/tApiZHnK9lvwbY2N
2bfg479r8OqhdL0a
2joShq78/toqBmUmE/6kjjI27u/R7AUlYQ831Jy1mkY
2o46IXwu/Jv1YAF9Q/R3FCKVz3/IG3YQ4C6nljRqFpa
3dai4QGX/gUBAibUF/M5duPh8Z/oyYpjmlyXPvbKzKt
3o2fWYXS/0M6O0tJ6FBXrNgmp
3o2fWYXS/fcm41ZuX/hjcdFzHMU5jV5SCL
43yCYsUZ/tX7PXd4b/JDRs4BLS/3MyAM8HjAzjNbXQ3
45R5wUnk/j1jBHze5SJGTJBFH
45R5wUnk/rfU9djVc/igQ1PCzr/L59IE6s9/NjN7R6vMtqBDxoI0
45R5wUnk/rfU9djVc/igQ1PCzr/UYyCIYY8BAeLdcxi
4EC71uyj/eSLibNo9/oy9koaAj/6YMDQ5l0/cjvzF2kUNPdE69m9
4Hd00u9x/gurApAAXD5QnnMqL
4jci5D5p/DrtbzlXm/bzOary7i/jGVAzSKuCv1gewno
5U6BXpb4/dcMrDnwwlFUJcdmm
60ouvgea/af3cN4Pq0i9GMBiL
6h7Q3QHRj6U0jczs
7WRvG3hdj4b0tBdk
7lJPPavUvleN9ZO9
87naoI4I/drpiEB3N/i9AeL1ur/dRg5CWvEiDPMb4R3
8IHeT2Ow9c3FLgWR
AQkGMZ9D/0kQAyIKu/P2Lrms4RksuviiZ7
Azy8VHGe/nzwVLw5N/3s2EKGNZ/rMsskE82/ZJ1Ey9O9NhCEFrfH
Cxh09zCv/2UQxnP29/pmOF983x/EsbiB5wy3zbDQPSM
Cxh09zCv/3SixpaCtcFsT6Alc
EA40LIedjsiVPgth
EerTfsxFQSzzl7Sq
FBWByU6u/3WjFSWkfnX6d1ENC
FBWByU6u/QAQjf3pj/rhXQBElwbbTD0bT6
Fe1iwzOb/eu0bBnNuhnhoZ5pQ
Fe1iwzOb/mryfmR4A/iU64ruAc/kXvTkigK/rit1uNEao2DkMflW
HFm4bBMf/no0X6oYu/bZTaJRbY/KGsndmWHR7cJxaS2
Hpmg3CpI/A6vewIhM/ZAePcATS/K8uoJ7Ow6W01aX24
IJMwIptp/v58kReQK/DlmlfGhP/uScvMBwGzT1r5h1o
JiZYfYXOUn733A7m
KIJdAdJT/Urp4f5u4rmR0YjdO
Lx4Rqol0/RlZpgk96L4gt8Yu5
M3tEZ0TC/RzR28nWczUODO7xk
MCCVL3Ju/KsdKvpWnLP6NQeI3
MCCVL3Ju/RbKJTdE3/qC1Ol8GK2Rwg7QDr
MElhjkUq/BVnaf7ko9Sq4vs45
MQBkun16k6kXXIwW
MYL79bn8/hYBFNkDU/I21hLgIv/a0oqfIPc/ocxQHPNikbqj0vq6
McBwAXer/gBC4C2ad/F9kFYySr/47gnnSdkqzHvkI3A
NAY7HbWk/hJss5QcP/6tS3DYJ61h2DH3NK
Q5kDiWyTfFvf8iNV
QJCMCBMg2xX4T9yu
QX4wTrGn/ZwGVQXar/AabkBNlw/Tgs1Mi8UCGdFPYV1
QX4wTrGn/ZwGVQXar/AabkBNlw/pYQtu9Om/b4OxFkjn6JCRjMMh
QX4wTrGn/ZwGVQXar/pZe5M58JPqT0POYr
RBHVEhs3NcQIy0l1
RdGk5R7N/T3UZ7pYU/ecughlt9/2vsv5nOiqZOFMebt
RdGk5R7N/T3UZ7pYU/ecughlt9/gP6aWwUa/EdQ8FipK9h806ruW
Slbo1ljG/O1GsECtk/EN4hz23a/HxTPuAVFcwj9kfX4
SuvLLi0N/dB0cE9TQYAnzseDp
TQC6PiEZ/pefcoOcY/Km2UGXgG/6pUHprrX/8D2zMQW6MyyZsw8d
Tf1INehNNcmFfjIG
UUwPzpyO/i92FrUJC/SEjYRJ6c/tnUO8smghprDCCwZ
WHefD3aT/ZDAfJTUq/JLVHlHwx5jli4JUb
WL6cv8KL/kpV4DTsZptoGUcGi
WSt6bJZveFE4LB2f
Wbk04Pig/Jp1qN1ro/bQ6Y6GdksvQDPWAc
WdOvYgiC/Eax1zeok2a6ETtqR
WkyJSmFbazDMTN9B
XdYRJYyC/HSDWpy0Xra5CM9Ce
Xkr5DVoh/ZCtf09eh/RECHauReEXpQr4GE
Xkr5DVoh/nWhgIcdkbDqhCdaB
Y7j18x6ObZaRhyeh
YQarDrEu/Qbhe7TtbfYvAdgRH
YaIkk4X4/5GW8Vxhv/XgnujZ96oMBBmfzH
Ydgq6Jvw/Sor8O93yJSdqIDEf
a2lGMUCW/feHUbJSc/uQKcBm3p/X6yEeSxsCKfJun45
a2lGMUCW/feHUbJSc/ub465UsnC6fnZd3u
bakOWubF/1OVD9jHE/QerffqIytUPlUjky
crgbIcuw/oLzR6cbk/JrMW7pco/wLBAn9Ad/WdMUBGeYMFFNnvQY
crgbIcuw/oLzR6cbk/dHOZNj3ya9lEKWAb
cvqaOLdV4rQwVFyD
d5vzb2n4/AadF2CGL/8AENWm0xP2EzY7hV
dCael6gU/1fwwVCKp/64cpUy2EuNV6S23Z
dCael6gU/1fwwVCKp/jbGfAjJE/7Yc51yezc0vNZsQL
dJJClgyQ/ltNgDMc3KyoKf7nq
eLChjGM7/ISNTiYFGHlm28a2O
ekNJUekt/7Fb20iBS/S6nevzfB/NeXQM9DETVUvWDCp
ekNJUekt/HcvAgUru38zzTBjh
f3iSZK6d/LDS5D5cQ/BLeLmrP94pcLeuZk
f3iSZK6d/LDS5D5cQ/KrPjEtno/fW5VvMke2Qyef6mP
fClQnLj1/9zi0d4Cv/Q81MfOLA/QdteYRi4e3GXYm0N
fClQnLj1/Gnw4oELXYKgRolVO
fb8pZC2Q/WElgNF68/4vYnJB00/3xuN7aXf/ZsHf7R4zsPk9OETM
htH4bRoN/mTXwuAeUQpE0Lz3u
i1BJiTNN/JgwAhUr0/GsCARxRt/4n4YuKuecShMysio
i1BJiTNN/q3TluS7h0atItCrm
iwFGVcel/YVMRJWCf/QTacAD1mGgNHZZUP
iwFGVcel/zi1A1QMBuU5Sb8Hn
jGlxIwrBznZsUMyK
k3egbwRD/8AYoy0vI/trfOBJ0n/csByahnv/Dyxh5w8BegSA0arl
kGsatlVI/9u9ofB0odGhV4p8A
kGsatlVI/fYx4qyQ7/ikPMQnfe/ss97ET1Jdcy8PHaK
koCpVSyPttmpSnKM
l4z5gx8UuQqYd9pX
l5QXAfJe/IUBF4WSFllXZeA91
lzFkih6I/aDIs9MZu/ZjvcShJw/kqoa96iw/OMjflf0az95CrdL9
m88KSMiL/lojDWAWg/UT6S6J03/RPUQ63Fd7AfEH9Gd
m88KSMiL/lojDWAWg/lHvpGE6IO5beaxLr
mYeGv8Hg/cjB9GvCQ/B0veveTKmGA8unFm
pWrPrqh1/U81QS2cefa1mdubo
pgcf8sf1/69Ksik1H/NSekMy3V/u4FrR1JF/ZKOWejqn8zeWBCbp
qdd5dLZa/73Qpx17cpP8r9Qm4
qg4lTHIP/RDXHI6aEZvfJIlHB
rVTJwYxr/RBgRP4cPftjomCQq
t3x4yjmE/YOYxA0g9/OdsCmIlatHmln24g
v9zZeb3A/2pCDNjnd/cdRY1kar1YC238im
vLtuuLIV/wKeFjaOb/Jh8Ydsif4Wc0VrgC
vbHOqs6E/NqUAOYUN/5KvzCc0z/IVSunAvCRWvJ765A
w4QoAoEB/xZ9wxz3M/h3eDnYXt/zZBViYCNnVCDQKL9
wv6NTnOR/yl2wi7uB/tsyjrNcL/aKzCUcnr/4lmfApblwhwc4UBC
y2KElVSQ/Sh3XY8uLLrgpMtMk
y2KElVSQ/XSH2RaDF/CNYDuHhW/USsnKmw9nWrvL5L4
ybywLwwY/ohcnociH/WM4htWMS/Ke14BW2z/DMDNDh1jdytc2UVB
ybywLwwY/ohcnociH/WM4htWMS/USN60itqqjnISnlR
z7MrkohzgMUHZZfN
"""

for bucket in buckets_name.split("\n"):
    if bucket:
        print("bucket item:",bucket)
        res = requests.get("http://challenge.ctf.games:32339/bucket/" + bucket)
        data = res.text

        if 'flag' in data:
            print(data)


