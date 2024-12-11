"""
Unfinished
"""

import os

class Object:
    def __init__(self, name: str, id: int, quantity: int, price: int, suplier: str, category: int):
        self.name = name
        self.id = id
        self.quantity = quantity
        self.price = price
        self.suplier = suplier
        self.category = category

    def __str__(self):
        return f"{self.name} ({self.category})"

def find_object_by_id(id):
    for obj in inventory:
        if obj.id == id:
            return obj
    return None

os.system('cls')
inventory = [
    Object("Chair", 0, 4, 50, "IKEA", "Furniture"),
    Object("Couch", 1, 1, 200, "IKEA", "Furniture"),
    Object("Table", 2, 1, 150, "IKEA", "Furniture")
    ]
unique = 3
running = True
while running:
    user = str(input("> "))
    if 'add' in user:
        prompt = user.split(" ")
        if len(prompt) != 6:
            print("Invalid arguments: add <name> <quantity> <price> <suplier> <catergory>")
            continue
        inventory.append(Object(prompt[1], unique, prompt[2], prompt[3], prompt[4], prompt[5]))
        unique += 1
    if 'edit' in user:
        prompt = user.split(" ")
        if len(prompt) != 3:
            print("Invalid arguments: edit <id> <quantity>")
            continue
        obj = find_object_by_id(int(prompt[1]))
        if obj == None:
            print(f"No object found '{prompt[1]}'")
            continue
        inventory.remove(obj)
        inventory.append(Object(obj.name, unique, prompt[2], obj.price, obj.suplier, obj.category))
        unique += 1
    if 'remove' in user:
        prompt = user.split(" ")
        if len(prompt) != 3:
            print("Invalid arguments: remove <id> <quantity>")
            continue
        obj = find_object_by_id(int(prompt[1]))
        if obj == None:
            print(f"No object found '{prompt[1]}'")
            continue
        if int(prompt[2]) > obj.quantity:
            print(f"Can't have negative quantity")
            continue
        if int(prompt[2]) == obj.quantity:
            inventory.remove(obj)
            continue
        index = inventory.index(obj)
        inventory[index] = Object(obj.name, obj.id, (obj.quantity - int(prompt[2])), obj.price, obj.suplier, obj.category)
        print(f"set {obj.name} quantity to {(obj.quantity - int(prompt[2]))} (from {obj.quantity}")
        continue
    if user == 'help':
        print("add <name> <quantity> <price> <suplier> <catergory>\nedit <id> <quantity>\nremove <id> <quantity>\nhelp\nlist\nexit\n")
        continue
    if user == 'list':
        for object in inventory:
            print(f"{object}   x{object.quantity}   id:{object.id}")
        print("\n")
        continue
    if user in ['exit', 'stop', 'bye']:
        running = False
        continue
    print("Unknown request:", user)