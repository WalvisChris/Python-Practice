"""
Joke generator from jokeapi.dev
"""

import os
import requests

os.system('cls')
URL = 'https://v2.jokeapi.dev/joke/Any?format=txt&type=single'
response = requests.get(URL)
if response.status_code == 200:
    print(response.text.strip())
else:
    print("Request failed")