# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
# in
# 9

# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

# in
# 10

# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]
from random import randint
import sys

def get_number(chislo):
    try:    
        int(chislo) 
        print('Ok')
        return int(chislo)
    except:
        print('The variable is not a number.')
        exit()
    

def my_list(number: int):
    nums_list = [randint(0, 30) for i in range(number)]
    print(nums_list)
    return nums_list

def max_number(nums_list: list):
    numbers_max = []
    nums_list_length = len(nums_list)
    i = 1
    while nums_list_length > i:
        if nums_list[i] > nums_list[i - 1]:
            numbers_max.append(nums_list[i])
            i += 1
        else:
            i += 1
            continue
    print(numbers_max)
    return numbers_max

def Main():
    enter = input('in: ')
    num = get_number(enter)
    max_number(my_list(num))
Main()
    