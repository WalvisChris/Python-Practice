import os

os.system('cls')
weaknesses = 0
password = str(input("Password: "))

# step 1: check for double characters
for i in range(len(password)-1):
    if password[i] == password[i+1]:
        weaknesses += 1

# step 2: check sorted streaks abc ABC 123
for i in range(len(password) - 2):
    if ord(password[i + 1]) - ord(password[i]) == 1 and ord(password[i + 2]) - ord(password[i + 1]) == 1:
            weaknesses += 1

# step 3: check length
if len(password) < 12:
     weaknesses += 12-len(password)

# step 4: check amount of different letters relative to length
freq = {}
for char in password:
     freq[char] = password.count(char)
for value in freq.values():
     if value > 2:
        weaknesses += value-2

# result
print(f"Weaknesses: {weaknesses}")