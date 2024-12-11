"""
Calculate average number
"""

import os

os.system('cls')
user = input("List: ")
user_list = [int(x) for x in user.split()]
print("Average:", (sum(user_list)/len(user_list)))