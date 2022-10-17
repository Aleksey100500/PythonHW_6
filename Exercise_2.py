# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
# in
# 100

# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100]

# in
# 424

# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100, 105, 120, 126, 140, 147, 160, 168, 180, 189, 200, 210, 220, 231, 240, 252, 260, 273, 280, 294, 300, 315, 320, 336, 340, 357, 360, 378, 380, 399, 400, 420]
from random import randint

def get_number():
    try:  
        number = int(input('in: '))  
        if number < 0:
            print('Ok')
            return abs(number)
        print('Ok')
        return number
    except:
        print('The variable is not a number.')
        exit()

def get_numbers(number: int):
    new_numbers = [randint(20, number) for i in range(number)]
    print(f'First list: \n{new_numbers}')
    second_numbers = [i for i in new_numbers if i % 20 == 0 or i % 21 == 0]
    print(f'Second list: \n{second_numbers}')

def Main():
    its_ok = get_number()
    get_numbers(its_ok)

Main()