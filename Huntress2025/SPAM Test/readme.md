## Chall description
```
Category: Warmups
Time to do some careful Googling... what's the MD5 hash of the Generic Test for Unsolicited Bulk Email (GTUBE) string?

Submit the hash wrapped within the flag{ prefix and } suffix to match the standard flag format.
```

## Procedure
Just looking for `Email spam tester GTUBE`, and you will get `https://spamassassin.apache.org/gtube/gtube.txt`.

```
## gbute.txt content

Subject: Test spam mail (GTUBE)
Message-ID: <GTUBE1.1010101@example.net>
Date: Wed, 23 Jul 2003 23:30:00 +0200
From: Sender <sender@example.net>
To: Recipient <recipient@example.net>
Precedence: junk
MIME-Version: 1.0
Content-Type: text/plain; charset=us-ascii
Content-Transfer-Encoding: 7bit

This is the GTUBE, the
	Generic
	Test for
	Unsolicited
	Bulk
	Email

If your spam filter supports it, the GTUBE provides a test by which you
can verify that the filter is installed correctly and is detecting incoming
spam. You can send yourself a test mail containing the following string of
characters (in upper case and with no white spaces and line breaks):

XJS*C4JDBQADN1.NSBN3*2IDNEN*GTUBE-STANDARD-ANTI-UBE-TEST-EMAIL*C.34X

You should send this test mail from an account outside of your network.

```

Get the md5 for `XJS*C4JDBQADN1.NSBN3*2IDNEN*GTUBE-STANDARD-ANTI-UBE-TEST-EMAIL*C.34X`

```
echo -n "XJS*C4JDBQADN1.NSBN3*2IDNEN*GTUBE-STANDARD-ANTI-UBE-TEST-EMAIL*C.34X" | md5sum

## output 
6a684e1cdca03e6a436d182dd4069183  -
```

Flag `flag{6a684e1cdca03e6a436d182dd4069183}`
