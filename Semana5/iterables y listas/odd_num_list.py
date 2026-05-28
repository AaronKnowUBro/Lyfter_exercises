my_num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

new_num_list = []

for num in my_num_list:
    if num % 2 == 0:
        new_num_list.append(num)

print("Lista solo con números pares:", new_num_list)
