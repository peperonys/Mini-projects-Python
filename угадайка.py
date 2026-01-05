from random import *

num = randint(1, 100)  # загадываем число
count = 0  # считаем количество попыток
print('Добро пожаловать в числовую угадайку!')

def is_valid(a1):
    if a1.isdigit():
        n = int(a1)
        if 1 <= n <= 100:
            return True
    return False

while True:
    a = input('Я загадал число в промежутке от 1 до 100. Угадай какое! ')
    
    if not is_valid(a):
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    
    a_num = int(a)
    count += 1
    
    if a_num > num:
        print('Ваше число больше загаданного, попробуйте еще разок')
    elif a_num < num:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    else:
        print('Вы угадали, поздравляем!')
        break

print(f'Количество попыток: {count}')
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')