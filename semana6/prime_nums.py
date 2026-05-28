def is_prime(num):
    if num <= 1:
        return False
    
    for divisor in range(2, int(num ** 0.5) + 1):   
        if num % divisor == 0:
            return False
    return True

def primes_in_list(numbers):
    return [n for n in numbers if is_prime(n)]

print(primes_in_list([1, 4, 6, 7, 13, 9, 67]))
