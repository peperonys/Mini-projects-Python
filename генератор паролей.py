from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

cntPw = int(input('Укажите количество паролей для генерации: '))
lenPw = int(input('Укажите длину одного пароля: '))
digOn = input('Включать ли цифры 0123456789? (y/n) ')
ABCon = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n) ')
abcOn = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n) ')
chOn = input('Включать ли символы !#$%&*+-=?@^_? (y/n) ')
excOn = input('Исключать ли неоднозначные символы il1Lo0O? (y/n) ')

if digOn.lower() == 'y':
    chars += digits
if ABCon.lower() == 'y':
    chars += uppercase_letters  #
if abcOn.lower() == 'y':
    chars += lowercase_letters  
if chOn.lower() == 'y':
    chars += punctuation
if excOn.lower() == 'y':
    # Удаляем неоднозначные символы
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

def generate_password(length, chars):
    pswrd = ''
    for _ in range(cntPw):
        password = ''
        for _ in range(length):
            password += choice(chars)
        pswrd += password + ' '
    return pswrd.strip()

print(generate_password(lenPw, chars))