# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки,
#  содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"

# out

def names_sort(names):
    sorted_names = sorted(names)
    return sorted_names

def new_dict(spisok_imen_sortirovanii):
    its_names_d = {}
    for name in spisok_imen_sortirovanii:
        key_d = name[0]
        if key_d not in its_names_d:
            its_names_d[key_d] = []
        its_names_d[key_d].append(name)
    return its_names_d

def Main():
    names = "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
    print(new_dict(names_sort(names)))
Main()
