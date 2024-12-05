import os

def verify(number):
    if number < 2:
        return False
    for i in range (2, number):
        if number%i==0:
            return False
    return True

os.system('cls')
number = int(input("number: "))
print(verify(number))