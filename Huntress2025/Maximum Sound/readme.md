## Chall description
```
Category: Warmups
Dang, this track really hits the target! It sure does get loud though, headphone users be warned!!
```

## Procedure
After try with a lot of stego tools, I decided to try with `SSTV`, and I was able to recover a `PNG` file with a stranger image.\
`sstv -d ~/Downloads/maximum_sound.wav -o ~/result.png`


<img width="320" height="256" alt="result" src="https://github.com/user-attachments/assets/8cc6ce71-562b-49be-a767-dec8121b25a1" />

After read about, I found this reference, this was a `MaxiCode`. Ahhhh that's why his name is `Maximum` 🫠
<img width="1764" height="958" alt="image" src="https://github.com/user-attachments/assets/4dba7d0f-91a5-4502-a707-ec28f5bfe380" />

Now I was able to recover the flag using this online [tool](https://products.aspose.app/barcode/recognize/maxicode#/recognized)
<img width="800" height="595" alt="Screenshot 2025-10-03 at 11 31 33 PM" src="https://github.com/user-attachments/assets/62442c4c-baf2-4a48-978c-029994ae0534" />

Flag `flag{d60ea9faec46c2de1c72533ae3ad11d7}`
