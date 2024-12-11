"""
Tells time
"""

import os
from datetime import datetime

os.system('cls')
now = datetime.now()
print(f"{now.strftime("%A")}, {now.strftime("%B")} {now.day}th, {now.year}, {now.hour}:{now.minute}")