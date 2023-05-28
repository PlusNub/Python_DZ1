# Требуется вычислить, сколько раз встречается некоторое число X в списке A.


# a = int(input('Ведите количество цифр: '))
# x = int(input('Введите искомое число: '))
# one_list = []
# for _ in range(a):
#     one_list.append(int(input()))
# print(one_list)
# new_list = one_list.count(x)
# print(new_list)



# Требуется найти в списке A самый близкий по величине элемент к заданному числу X




a = int(input('Ведите количество цифр: '))
x = int(input('Введите число для сравнения: '))
one_list = []
for _ in range(a):
    one_list.append(int(input()))
print(one_list)
num = one_list[0]
for elem in one_list:
    if abs(elem - x) < abs(num - x):
     num = elem
print(num)     



