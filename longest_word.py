import os

os.system('cls')
sentence = str(input("sentence: "))
words = sentence.split(" ")
length = [len(word) for word in words]
longest = max(length)
index = length.index(longest)
print(f"Longest: {words[index]}, length: {length[index]}")