import os
import time

def visualize(list, index, passes):
    os.system('cls')
    for i, item in enumerate(list):
        text = "\033[32m███" * int(item) + "\033[0m" if i-1 == index or i == index else "███" * int(item)
        print(text)
    print("Pass:", passes)

os.system('cls')
user = input("List: ")
sort = user.split()
passes = 0
unsorted = True
while unsorted:
    flag = False
    for i in range(len(sort)-1):
        visualize(sort, i, passes)
        a = sort[i]
        b = sort[i+1]
        if a>b:
            sort[i] = b
            sort[i+1] = a
            flag = True
        #time.sleep(.1)
        visualize(sort, i, passes)
        #time.sleep(.1)
    passes += 1
    unsorted = flag
visualize(sort, 0, passes)