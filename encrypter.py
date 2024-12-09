import os

os.system('cls')
message = str(input("message: "))
shift = int(input("shift: "))

result = ""
for char in message:
    if char == ' ':
        result += char
        continue
    old = ord(char)
    new = old + shift
    if new > 122:
        new -= 26
    elif new < 97:
        new += 26
    result += chr(new)
print("Result:\n" + result)