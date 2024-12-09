import os
import time

def show(s):
    os.system('cls')
    print(s)

spinner = ["|", "/", "-", "\\"]

message = "hello world"

frame = 0
while True:
    msg = ""
    for i, char in enumerate(message):
        msg += char.upper() if i == frame % len(message) else char
    show(f"{spinner[frame % len(spinner)]}\n{msg}\n{(frame % 9)+1}")
    frame += 1
    time.sleep(0.1)