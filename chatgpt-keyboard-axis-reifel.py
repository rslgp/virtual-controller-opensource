#coded by Reifel https://steamcommunity.com/profiles/76561197987727467/myworkshopfiles/?appid=108600
import pyvjoy
import pyautogui
import keyboard
import threading
import time
import win32api

isLeftAnalogStick = False

j = pyvjoy.VJoyDevice(1)

stop_threads = False

def press_button(key, button_num):
    if keyboard.is_pressed(key):
        j.data.lButtons |= 1 << (button_num - 1)
    else:
        j.data.lButtons &= ~(1 << (button_num - 1))

def read_keyboard():
    global j
    #key binds
    #' 1 to 9, z x c v b, f g h
    buttons = ['\'', '1', '2', '3', '7', 'x', 'v', 'b', 'c', '4', '5', 'f', 'h', '9', 'z', '6', '8', 'g']
    global stop_threads
    while not stop_threads:
    #while True:
        for i, key in enumerate(buttons):
            press_button(key, i+1)
        j.update()
        time.sleep(0.01)

screen_width = win32api.GetSystemMetrics(0)
screen_height = win32api.GetSystemMetrics(1)
max_value = 32767

cte1 = max_value / screen_width
cte2 = max_value / screen_height


def read_mouse():
    global j
    global stop_threads
    while not stop_threads:
        x, y = win32api.GetCursorPos()
            
        # Map the mouse position to the range of the analog stick
        x_axis = int(x * cte1)
        y_axis = int(y * cte2)
        
        if(isLeftAnalogStick):
            j.data.wAxisX = x_axis
            j.data.wAxisY = y_axis
        else:
            # Set the value of the Right Analog Stick on the virtual joystick
            j.data.wAxisXRot = x_axis
            j.data.wAxisYRot = y_axis
        #j.update()

# Function to stop threads
def stop_all_threads():
    global stop_threads
    stop_threads = True

keyboard.add_hotkey('F1', stop_all_threads)
# Create and start the keyboard input thread
keyboard_thread = threading.Thread(target=read_keyboard)
keyboard_thread.start()

# Create and start the mouse input thread
mouse_thread = threading.Thread(target=read_mouse)
mouse_thread.start()

def link(uri, label=None):
    if label is None: 
        label = uri
    parameters = ''

    # OSC 8 ; params ; URI ST <name> OSC 8 ;; ST 
    escape_mask = '\033]8;{};{}\033\\{}\033]8;;\033\\'

    return escape_mask.format(parameters, uri, label)
print("\nOpensource Virtual Controller for Zomboid by modder Reifel is running");
print("PRESS F1 to exit");
