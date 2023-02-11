# virtual-controller-opensource
a virtual controller opensource coded by bsc Computer Science with pair programming with chatgpt, for debug zomboid mods, with changeable axis (L analog or R analog) for mouse

press F1 to exit

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
pip install -r requirements.txt
python chatgpt-keyboard-axis-reifel.py

Showcase:
https://user-images.githubusercontent.com/11529665/218254861-4a08a6fa-582d-48b3-b565-884ca27f4a88.mp4

