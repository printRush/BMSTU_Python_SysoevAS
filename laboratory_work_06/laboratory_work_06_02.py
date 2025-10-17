with open('input4.txt', 'r') as f:
    arr = list(map(float, f.read().split(', ')))

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

# sort 0 + others
zeros = [x for x in arr if x == 0]
others = [x for x in arr if x != 0]
result = zeros + others


with open('output4.txt', 'w+') as f:
    f.write(f'Минимальный элемент: {min(arr)} \n'
                 f'\nСумма чисел: {sum_of_pos_nums}\n'
            f'\nОтсортированный массив: {result}\n\n\n')

print("Done!")
