"""
Bubble sort custom list
"""

import os

os.system('cls')
user = input("List: ")
sort = user.split()
passes = 0
unsorted = True
while unsorted:
    flag = False
    for i in range(len(sort)-1):
        a = sort[i]
        b = sort[i+1]
        if a>b:
            sort[i] = b
            sort[i+1] = a
            flag = True
    passes += 1
    unsorted = flag
print(f"Pass {passes}: {sort}")