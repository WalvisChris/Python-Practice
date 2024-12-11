"""
Shows the calenders month view
"""

import os
import calendar

os.system('cls')
year = int(input("Year: "))
month = int(input("Month: "))

x, current_days = calendar.monthrange(year, month)
y, previous_days = calendar.monthrange(year, month-1)
z, next_days = calendar.monthrange(year, (month%12)+1)

current_list = list(range(current_days))
previous_list = list(range(previous_days))[-x:] # borrow from previous month
next_list = list(range(next_days))

total_list = previous_list + current_list
line = ""

os.system('cls')
print(f"\033[33m{str(f"{calendar.month_name[month]} {year}").center(26)}\033[0m")
print("\033[33mmo  tu  we  th  fr  sa  su\033[0m")
for count, day in enumerate(total_list):
    line += "\033[90m" + str(day+1).rjust(2) + "\033[0m  " if count < x else str(day+1).rjust(2) + "  " # color previous days
    if (count+1)%7==0:
        print(line)
        line = ""
    if count+1 == len(total_list):
        leftover = (7 - (len(total_list) % 7)) % 7 # add empty leftovers, another %7 because 7 leftovers is impossible
        if leftover != 0:
            for x in next_list[:leftover]:
                line += "\033[90m" + str(x+1).rjust(2) + "\033[0m  " # color leftover days
            print(line)
print("\n")