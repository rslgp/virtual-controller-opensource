# virtual-controller-opensource
a virtual controller (joystick with two analog stickers) opensource coded by bsc Computer Science with pair programming with chatgpt, for debug zomboid mods, with changeable axis (L analog or R analog) for mouse

```
press F1 to exit
keybinds: ' 1 to 9, z x c v b, f g h
```

userful for debug if you dont have controller, you can test axis using mouse, and to change analog stick change in code 

or just add "right" argument as parameter (...).py right or (...).exe right (without quotes)
```
isLeftAnalogStick=False
to
isLeftAnalogStick=True
``` 
for modders that dont have controller to test with, this works for simulate controller
i bsc computer science pair programming with chatgpt to produce a python joystick keyboard opensource, to work with vjoy, enjoy

to debug using a virtual controller, to got 99.9% precision use your window screen monitor borders, 

##### LOOKING FOR PR: 
someone can try optimize the precision using math and screen knowledge (hint you can reduce the screen to fit better the circle of radial menu)

##### setup and install
requirements: [vjoy needed](https://sourceforge.net/projects/vjoystick/files/latest/download) 
config vjoy 18 buttons 
to run, install python

```
pip install -r requirements.txt

left analog stick:
python chatgpt-keyboard-axis-reifel.py

right analog stick:
python chatgpt-keyboard-axis-reifel.py right
```
or
##### [portable executable](https://github.com/rslgp/virtual-controller-opensource/releases/download/v1.0/chatgpt-keyboard-axis-reifel.exe) + [vjoy needed](https://sourceforge.net/projects/vjoystick/files/latest/download) 
```
no need python installed
run release executable

left analog stick:
chatgpt-keyboard-axis-reifel.exe

right analog stick:
chatgpt-keyboard-axis-reifel.exe right

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

