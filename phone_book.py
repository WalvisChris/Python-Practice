"""
Simple phone book, add remove show bye
"""

import os

phonebook = [['Max', 2895374491, 'Detroit'],
             ['Angela', 1928553692, 'Paris'],
             ['Greg', 9271655473, 'London']]

def find_in_phonebook(target):
    target = int(target) if target.isdigit() else str(target).lower() if isinstance(target, str) else target
    for i, person in enumerate(phonebook):
        for data in person:
            data = str(data).lower() if isinstance(target, str) else data
            if data == target:
                return i
    return -1

os.system('cls')
running = True
while running:
    user = str(input("> "))
    os.system('cls')
    command = user.split(" ")
    if command[0] == 'add':
        if len(command) != 4:
            print(f"Invalid arguments: add <name> <number> <city>")
            continue
        if not command[2].isdigit():
            print(f"number '{command[2]}' is not a number")
            continue
        if len(command[2]) != 10:
            print(f"Invalid phone number: {command[2]}")
            continue
        phonebook.append([command[1], command[2], command[3]])
        print("Added", command[1], "to the phonebook.")
    elif command[0] == 'remove':
        if len(command) != 2:
            print(f"Invalid arguments: remove <name>")
            continue
        index = find_in_phonebook(command[1])
        if index == -1:
            print(f"'{command[1]}' not in phonebook")
            continue
        phonebook.pop(index)
        print("removed:", command[1])
    elif command[0] == 'show':
        print("<name> <number> <city>\n")
        for person in phonebook:
            print(f"{person[0]}: {person[1]} ({person[2]})")
        print("\n")
    elif command[0] in ['stop', 'exit', 'bye']:
            running = False