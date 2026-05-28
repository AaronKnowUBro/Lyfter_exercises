user_num = int(input("por favor digite el numero para la suma: "))

sum = 0
total_sum = 0

for counter in range(1, user_num + 1):
    total_sum = total_sum + counter

print(f"La suma desde 1 hasta {user_num} es de {total_sum}")