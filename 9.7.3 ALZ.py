number = 23
running = True
while running:
    guess = int(input('Введите целое число:'))
    if guess == number:
        print('Поздравляю, вы угадали.')
        running = False # останавливает цикл while
    elif guess < number:
        print('Нет, число немного меньше этого')
    else:
        print('Нет, число немного больше этого.')
else:
    print('Цикл while закончен.') # Здесь можно выполнить все что нужно
    print('Завершение.')
