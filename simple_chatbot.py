import os

responses = {
    "hello": "Hi there! How are you?",
    "hi": "Hi there! How are you?",
    "hey": "Hi there! How are you?",
    "how are you": "I'm good! How about you?",
    "fart": "I won't tell anyone."
}

os.system('cls')

running = True
while running:
    user = str(input("You: ")).lower()
    if user in ['bye', 'goodbye', 'stop', 'exit']:
        running = False
        continue
    elif user in responses.keys():
        print(f"Bot: {responses[user]}")
    else:
        print(f"Bot: I don't understand '{user}'")
print("Bot: Goodbye!")