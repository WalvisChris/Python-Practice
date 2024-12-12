"""
Counts down from 'n'
"""

import os
import time
import math

os.system('cls')
n = float(input("Time? "))
start = time.time()

running = True
while running:
    os.system('cls')
    now = time.time()
    timeToDisplay = math.ceil(n - (now - start))
    print(timeToDisplay)
    if timeToDisplay < 1:
        running = False
    time.sleep(1)