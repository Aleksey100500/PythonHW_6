from random import randint
nums_list = [randint(0, 30) for i in range(10)]
print(nums_list)
numbers_max = [i for i in nums_list if i > i ]
print(numbers_max)