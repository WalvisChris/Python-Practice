import os

os.system('cls')
screen = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

def handle(direction):   
    if direction == 'up':
        print("fart")

def spawn():
    print("random")

def display():
    print(screen)

running = True
while running:
    user = str(input("move: "))
    if user in ['up', 'down', 'left', 'right']:
        handle(user)
    elif user in ['exit', 'stop']:
        running = False
    else:
        print("Invalid:", user)
print("Thank you for playing!")