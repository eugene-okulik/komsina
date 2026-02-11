stored_number = 8
while True:
    user_input = int(input('Input your number '))
    if user_input == stored_number:
        print('Поздравляю! Вы угадали!')
        break
    elif user_input != stored_number:
        print('Попробуйте снова')
