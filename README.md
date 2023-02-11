# virtual-controller-opensource
a virtual controller opensource coded by bsc Computer Science with pair programming with chatgpt, for debug zomboid mods, with changeable axis (L analog or R analog) for mouse

press F1 to exit
keybinds: ' 1 to 9, z x c v b, f g h

userful for debug if you dont have controller, you can test axis using mouse, and to change axis change in code
```
isLeftAnalogStick=False
to
isLeftAnalogStick=True
``` 
for modders that dont have controller to test with, this works for simulate controller
i bsc computer science pair programming with chatgpt to produce a python joystick keyboard opensource, to work with vjoy, enjoy

to debug using a virtual controller, to got 99.9% precision use your window screen monitor borders, someone can try optimize the precision using math and screen knowledge (hint you can reduce the screen to fit better the circle of radial menu)

requirements: vjoy https://sourceforge.net/projects/vjoystick/files/latest/download config 18 buttons there
to run, install python

```
pip install -r requirements.txt
python chatgpt-keyboard-axis-reifel.py
```
or
```
no need python installed
run release executable
chatgpt-keyboard-axis-reifel.exe
```

Showcase:



https://user-images.githubusercontent.com/11529665/218254946-39857009-b4fe-49d2-8dbd-82ad02827fd0.mp4

```
key binds map:
' : A
1 : B
2 : x
3 : y
7 : L
x : R
v : ZL
b : ZR
c : +
4 : -
5 : L-Click
f : R-Click
h : D-Up
9 : D-Down
z : D-Left
6 : D-Right
8 : blow-mic
g : Show-Screen
```

