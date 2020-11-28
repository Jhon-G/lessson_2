age = int(input('Enter you age: '))

def type_of_life(age):
    if age <= 0:
        raise ValueError("Your age cannot be lower than 0")
    elif age <= 6:
        return f'Wake up you go to kindergarten'
    elif age > 6 and age <= 18:    
        return f'Hurry up you must be in school'
    elif age > 18 and age <= 25:
        return f'Congratulations you in university'
    else:
        return f'You need to find job'


result = type_of_life(age)
print(result)
