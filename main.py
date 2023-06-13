# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.

def fill_array(n,mn,mx):
    import random
    array = [random.randint(mn, mx) for _ in range(n)]
    return array

n = int(input())
m = int(input())

list1 = fill_array(n, 2, 13)
list2 = fill_array(m, 2 ,13)
print(list1)
print(list2)

set1 = set(list1)
set2 = set(list2)

result = set1 & set2
print(result)
    