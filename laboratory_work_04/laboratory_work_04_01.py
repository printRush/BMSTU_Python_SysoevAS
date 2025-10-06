from random import *

n = int(input("Элементов в массиве(N<=30) N: "))

if n > 30:
    n = 30
elif n < 5:
    n = 5

arr = [uniform(-5, 5) for i in range(n)]

print(arr)

# min
print("\nМинимальный элемент: ", min(arr), '\n')

# sum of numbers
sum_of_pos_nums = 0

first_positive_index = 0

for i in range(len(arr)):
    if arr[i] > 0:
        first_positive_index = i
        break

last_positive_index = len(arr) - 1

for j in range(len(arr)):
    if arr[j] > 0:
        last_positive_index = j

for k in range(first_positive_index + 1, last_positive_index):
    sum_of_pos_nums += arr[k]


print(first_positive_index, arr[first_positive_index])
print(last_positive_index, arr[last_positive_index])

print("\nСумма чисел: ", sum_of_pos_nums)

# sort 0 + others
zeros = [x for x in arr if x == 0]
others = [x for x in arr if x != 0]
result = zeros + others

print('\nОтсортированный массив: ', result)

