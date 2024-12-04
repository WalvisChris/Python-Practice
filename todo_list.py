import os

def ask():
    user = input("todo> ")
    if 'add' in user:
        parameters = user.split()
        if len(parameters) != 3:
            print("Invalid parameters: add <name> <description>")
        else:
            tasks[parameters[1]] = parameters[2]
    elif 'remove' in user:
        parameters = user.split()
        if len(parameters) != 2:
            print("Invalid parameters: remove <name>")
        else:
            del tasks[parameters[1]]
    elif user == 'view':
        print(tasks)
    elif user == 'help':
        print("- view: shows todo list\n- add <name> <description>: adds to todo list\n- remove <name>: removes from todo list")
    else:
        print(f"Unknown command: {user}")
    ask()

tasks = {}

os.system('cls')
ask()