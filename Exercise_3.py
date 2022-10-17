# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки,
#  содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"

# out

# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}
names = "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
sorted_names = sorted(names)
result_letters = []
for name in sorted_names:
    result_letters.append(name[0])
its_names_d = dict.fromkeys(result_letters)
for key in its_names_d:
    i = 0
    # for name in sorted_names:
    if key != sorted_names[i]:
        its_names_d[key] = sorted_names
        i += 1
def function(name):
    return name[0]  

print(its_names_d)

