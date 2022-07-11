# This is the game "Guess the number!"

from random import randint


def is_valid(n):
    return n.isdigit() and 1 <= int(n) <= int(l_p)

def is_valid_right_limit():
    global l_p
    l_p = input()
    if l_p.isdigit() and 1 < int(l_p):
        return int(l_p)

def guess():

    print('Добро пожаловать в игру числовая угадайка!')
    print('Выберите правую границу для диапазона чисел. Введите целое положительное число, больше 1...')
    a = randint(1, is_valid_right_limit())
    print(f'Угадывайте! Введите число от 1 до {int(l_p)} включительно')
    counts = 0
    while True:
        s = input()
        counts += 1
        if is_valid(s):
            s = int(s)
        else:
            print(f'А может быть все-таки введем целое число от 1 до {int(l_p)}?')
            continue
        if s < a:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif s > a:
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif s == a:
            print('Вы угадали, поздравляем!')
            break
    print('Количество использованных попыток:', counts)
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
    print()
    print('Хотите сыграть еще? Введите единицу, если да, или ноль, если нет')
    x = int(input())
    if x:
        guess()
    else:
        print('Всего доброго!')


guess()
