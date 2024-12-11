"""
Displays who won based on votes
"""

import os
import math

votes = {"team blue": 0, "team red": 0}
os.system('cls')
t1 = int(input("Team blue votes: "))
t2 = int(input("Team red votes: "))
total = t1 + t2
bar_width = 20
if t1 > t2:
    print("Team \033[94mblue\033[0m won!")
    blue_bars = math.ceil((t1 / total) * bar_width)
    red_bars = bar_width - blue_bars
    print("\033[94m█\033[0m" * blue_bars + "\033[91m█\033[0m" * red_bars)
else:
    print("Team \033[91mred\033[0m won!")
    red_bars = math.ceil((t2 / total) * bar_width)
    blue_bars = bar_width - red_bars
    print("\033[91m█\033[0m" * red_bars + "\033[94m█\033[0m" * blue_bars)