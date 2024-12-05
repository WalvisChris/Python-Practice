import os

invalid = list(range(32, 64))
invalid.extend([96, 123, 125, 126])
invalid.remove(46)

def verify(email):
    format = ''.join([char for char in email if char == '.' or char == '@'])
    if format != '.@.':
        print("not .@.")
        return False
    at = email.find("@")
    if email[at-1] not in 'abcdefghijlkmnopqrstuvwxyz' or email[at+1] not in 'abcdefghijlkmnopqrstuvwxyz':
        print("incorrect text placement")
        return False
    for char in email:
        if ord(char) in invalid:
            print("in invalid")
            return False
    return True

os.system('cls')
email = str(input("email: "))
print(verify(email))