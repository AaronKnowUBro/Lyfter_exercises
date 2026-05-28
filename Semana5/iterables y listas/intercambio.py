my_list = [10, 20, 30, 40, 50]
my_second_list = [100, 300, 500, 400, 70]

if len(my_list) > 1:
    temp = my_list[0]
    my_list[0] = my_list[-1]
    my_list[-1] = temp

print("Lista después del intercambio:", my_list)


if len(my_list) > 1:
    my_second_list[0], my_second_list[-1] = my_second_list[-1], my_second_list[0]

print("Lista después del intercambio:", my_second_list)
