## Name: Kitty Kitty Bang Bang
#### Category: Mobile
#### Difficulty: easy
#### Description: I found a cool android app to play with a cowboy cat! There's has to be more going on with the app I can't see on my screen...

## Procedure
We can see an APK file, the decription chall talks about "something else I cant see on my screen", I will recover the apk code using the site ```http://www.javadecompilers.com/apk```<br>

<img width="925" alt="Screenshot 2024-05-26 at 16 42 18" src="https://github.com/sp34rh34d/CTF-writeups/assets/94752464/df74fcdd-0a53-4e99-bf50-c4cec2785eb7">
<br>

Go the path ```sources/com/nahamcon2024/kittykittybangbang/``` and take a look to file ```MainActivity.java```.
<br>

## MainActivity.java Content
1) onCreate$lambda$0: Handles touch events, logs a message when a tap is detected.
2) Calls showOverlayImage() to display the overlay image.
3) Calls playSound(R.raw.bang) to play a sound.
4) Logs a message containing our flag fetched from the native method stringFromJNI().
5) stringFromJNI(): A native method that likely returns a string from a native library loaded at the end of the class.
   
```
public final native String stringFromJNI();

public static final boolean onCreate$lambda$0(MainActivity mainActivity, View view, MotionEvent motionEvent) {
        Intrinsics.checkNotNullParameter(mainActivity, "this$0");
        Log.i("kitty kitty bang bang", "Listening for taps...");
        if (motionEvent.getAction() != 0) {
            return true;
        }
        Log.i("kitty kitty bang bang", "Screen tapped!");
        mainActivity.showOverlayImage();
        mainActivity.playSound(R.raw.bang);
        Log.i("kitty kitty bang bang", "BANG!");
        Log.i("kitty kitty bang bang", "flag{" + mainActivity.stringFromJNI() + '}');
        return true;
    }
```
<br>

Now we just need to emulate the app and see the app logs to recover our flag, i will use Android Studio for it. 

<img width="1078" alt="Screenshot 2024-05-26 at 17 00 41" src="https://github.com/sp34rh34d/CTF-writeups/assets/94752464/b41affa6-d82e-476d-abaf-4baf08c201fd">
<br>

Copy the app log, and just search for ```flag{``` word.

<img width="704" alt="Screenshot 2024-05-26 at 17 01 29" src="https://github.com/sp34rh34d/CTF-writeups/assets/94752464/344e2fa0-9238-417d-aa0b-e730e60d1d60">
<br>

flag ```flag{f9028245dd46eedbf9b4f8861d73ae0f}```




