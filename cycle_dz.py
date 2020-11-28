print('Задание № 1')
def hello_user():
    try:
        while True:
            user_say = input('Как дела ? ')
            user_say = user_say.capitalize()
            if user_say == 'Хорошо':
                break
            else:
                print(f'Сам ты {user_say}')
    except KeyboardInterrupt:
        print('Пока', end= print())

hello_user()

print('Задание № 2')

faq = {
    'Как дела': 'Хорошо!',
    'Что делаешь':'Прогриммирую',
}


def ask_user():
    while True:
        question = input('Спроси меня: ')
        if question in faq:
            print(faq[question])
            break
        else:
            print('Спроси еще что нибудь')

ask_user()