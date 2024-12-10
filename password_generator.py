"""
random string generator from list of characters of length 'n'
"""

import os
import random

os.system('cls')
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJLKMNOPQRSTUVWXYZ`~1!2@3#4$5%6^7&8*9(0)-_=+[{]}\|;:',<.>/?\|"
user = int(input("Password length? "))
password = ""
for i in range(user):
    password += characters[random.randint(0, len(characters)-1)]
print(password)