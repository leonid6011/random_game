import random

def is_valid(num):
    if num.isdigit() and 1 <= int(num) <= 100:
        return True
    else:
        return False

print('Добро пожаловать в числовую угадайку')
flag = False
NBR_VAL = random.randint(0, 100)
count = 0
while not flag:
    print('Введите число от 1 до 100:')
    nbr = input()
    if not is_valid(nbr):
        print('А может быть все-таки введем целое число от 1 до 100?')
    else:
        nbr = int(nbr)
        if nbr > NBR_VAL:
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif nbr < NBR_VAL:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            flag = True
    count += 1
print('Спасибо, что играли в числовую угадайку. Число попыток:', count)
print('Еще увидимся...')