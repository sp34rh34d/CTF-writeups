## Name: 3D Obj
#### Category: forensic
#### Difficulty: N/A
#### Description: I am sending you my secret cube. I hope you could read my secret from the little colourful squares?

## Procedure
The ```.mtl``` file is a material library file used in 3D modeling. It is associated with the ```.obj``` file format, which defines the geometry of a 3D model. The ```.mtl``` file describes the surface appearance of the 3D object, including colors, textures, reflectivity, and other material properties.

```
├── chall
│   ├── chall.obj
│   ├── cube.mtl
│   └── tex.png
```


### chall.obj content
```
cat chall.obj | head -n 20
mtllib cube.mtl
g cube
v 25.818113 -1.852144 -9.649591
v 26.695771 -2.219219 -9.957767
v 27.573428 -2.586295 -10.265943
v 28.451086 -2.953371 -10.574119
v 29.328744 -3.320447 -10.882295
v 30.206401 -3.687522 -11.190471
v 31.084059 -4.054598 -11.498647
v 31.961717 -4.421674 -11.806823
v 32.839374 -4.788750 -12.114999
v 33.717032 -5.155825 -12.423176
v 34.594689 -5.522901 -12.731352
v 35.472347 -5.889977 -13.039528
v 36.350005 -6.257052 -13.347704
v 37.227662 -6.624128 -13.655880
v 38.105320 -6.991204 -13.964056
v 38.982978 -7.358280 -14.272232
v 39.860635 -7.725355 -14.580408
v 40.738293 -8.092431 -14.888584
```

### cube.mtl content
```
newmtl texture
Ka 0.0 0.0 0.0
Kd 0.5 0.5 0.5
Ks 0.0 0.0 0.0
Ns 10.0
illum 2
map_Kd tex.png
```

I have used the site [3dviewer](https://3dviewer.net) to load the files and try to figure out my flag

<img width="1672" alt="Screenshot 2024-09-03 at 8 57 59 PM" src="https://github.com/user-attachments/assets/e0d7e868-d477-456b-b79b-57c1a23ec20e">

now time to shake it baby

<img width="384" alt="Screenshot 2024-09-03 at 8 58 42 PM" src="https://github.com/user-attachments/assets/6e763cf2-04a7-48b8-87a1-43859bea3e0d">
<br>

After a few minutes and 20 failed attempts to submit the flag 💀🫠😂... ```@Trap, sorry bro``` 
![ScreenRecording2024-09-03at8 53 59PM-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/b89255ad-2b75-4a9d-a684-843ab34da8eb)


flag ```CSCTF{H1d1ng_in_T3x7ur3}```

