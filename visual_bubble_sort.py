import os
import time

def visualize(list, index, passes):
    buffer = ""
    for i, item in enumerate(list):
        buffer += "\033[32m███" * int(item) + "\033[0m" if i-1 == index or i == index else "███" * int(item)
        buffer += "\n"
    os.system('cls')
    print(buffer)
    print("Pass:", passes)

os.system('cls')
#user = input("List: ")
#sort = user.split()
sort = [9, 7, 5, 5, 6, 4, 3, 7, 9, 6, 4, 5, 5, 3, 7, 4, 2, 7, 6, 5]
passes = 0
unsorted = True
while unsorted:
    passes += 1
    flag = False
    for i in range(len(sort)-1):
        visualize(sort, i, passes)
        a = sort[i]
        b = sort[i+1]
        if a>b:
            sort[i] = b
            sort[i+1] = a
            flag = True
        visualize(sort, i, passes)
    unsorted = flag
visualize(sort, 0, passes)