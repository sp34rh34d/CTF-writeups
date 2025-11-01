## Chall description
```
Category: OSINT
Hey Support Team,
Thanks for your help the other day! After seeing the way you handled yourself and gathered these details, I wanted to see if I could get a bit more help from you. I know you found their username the other day. See what you can do with that. I need you to find the town that this hacker lives in. I don't think the IR firm is doing enough. I want to have every piece of information we can find. Maybe we can pay a visit. Let me know what you find. Thanks!
```
## Procedure
The previous chall, we find the username `N0TrustX`, We were using `Sherlock` but no luck, then we try looking for `N0TrustX` on Twitter and we find 1 match.
<img width="712" height="184" alt="Screenshot 2025-10-29 at 6 41 44 PM" src="https://github.com/user-attachments/assets/3481c694-51c1-44fc-817c-7616254e629e" />

The profile has an string encoded using octal `111 40 141 155 40 164 150 145 40 157 156 145 40 167 150 157 40 153 156 157 143 153 163`, but nothing interesting.
<img width="1361" height="561" alt="Screenshot 2025-10-29 at 6 43 16 PM" src="https://github.com/user-attachments/assets/42530a40-5685-4f88-bac2-485454842e13" />

Reading every post, we can see reference to `coffee (java)`, but the hacker takes some photographs, we can try reading metadata or using Google Image finder

<img width="604" height="299" alt="Screenshot 2025-10-29 at 6 46 47 PM" src="https://github.com/user-attachments/assets/bcd05e9b-dc13-47d7-8716-3eb0928da599" />

<img width="603" height="632" alt="Screenshot 2025-10-29 at 6 47 05 PM" src="https://github.com/user-attachments/assets/0935251a-61eb-4640-a4fb-4f8c9f937e44" />

<img width="600" height="418" alt="Screenshot 2025-10-29 at 6 47 16 PM" src="https://github.com/user-attachments/assets/3ed5e52d-dfb7-416b-8a6b-d5ee350e19e5" />

Finally we have found the place where 1 photo was taked. this has reference to `Wytheville`, **What town does our hacker friend live in? = Wytheville**

<img width="626" height="643" alt="Screenshot 2025-10-29 at 7 01 48 PM" src="https://github.com/user-attachments/assets/f789bb61-9fde-473f-aa61-c77332db7abb" />

Using Google Maps, we can try to find any `coffee` shop on `Wytheville`, and we can see a coffee shop called `The Grind`, yeah we have seen this name on hacker account post.
<img width="1781" height="806" alt="Screenshot 2025-10-29 at 7 03 04 PM" src="https://github.com/user-attachments/assets/a06d2e9c-25f7-4330-9989-d7b4fbcd777a" />

Search for `The Grind` and filtering for `flag` on `Opinions` tab, we finally find our flag.
<img width="1572" height="979" alt="Screenshot 2025-10-29 at 7 18 18 PM" src="https://github.com/user-attachments/assets/5b5e437f-8cfc-46d4-bf99-c7d46408912c" />

Flag `Flag{this_is_good_java}`
