def comparing(string1, string2, learn = 'learn'):
    if type(string1 or string2) is not str: #Check type of arguments
        return 0
    elif string1.lower() == string2.lower():
        return 1
    elif string2.lower() != learn: # if 2nd string not lear go to if
        if string1.lower() != string2.lower() and len(string1) > len(string2):
            return 2
    elif string1.lower() != string2.lower() == learn:
        return 3


print(comparing(1, 2.5))
print(comparing('Hello', 'Hello'))
print(comparing('Привет','Hello'))
print(comparing('Python', 'Learn'))



