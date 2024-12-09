import os
from pynput import keyboard

def on_press(key):
    global result
    if key == keyboard.Key.enter:
        print(f"Keys recorderd:\n\n{result}")
        exit()
    elif key == keyboard.Key.space:
        result += " "
        return
    result += key.char

os.system('cls')
result = ""
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
        