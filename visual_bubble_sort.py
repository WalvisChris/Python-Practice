import os
import time

def visualize(list, index):
    os.system('cls')
    for i, item in enumerate(list):
        text = "\033[32m██" * int(item) + "\033[0m" if i == index or i+1 == index else "██" * int(item)
        print(text)

os.system('cls')
user = input("List: ")
sort = user.split()
passes = 0
unsorted = True
while unsorted:
    flag = False
    for i in range(len(sort)-1):
        visualize(sort, i)
        a = sort[i]
        b = sort[i+1]
        if a>b:
            sort[i] = b
            sort[i+1] = a
            flag = True
        time.sleep(0.1)
        visualize(sort, i)
        time.sleep(0.1)
    passes += 1
    unsorted = flag
visualize(sort, 0)
print(f"Pass {passes}: {sort}")