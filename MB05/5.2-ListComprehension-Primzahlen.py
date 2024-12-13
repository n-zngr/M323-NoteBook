import random

numbers = random.sample(range(1, 51), 50)
sorted_numbers = sorted(numbers)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(numbers):
    
    return [num for num in numbers if is_prime(num)]

primes = find_primes(sorted_numbers)
print("Sorted List:", sorted_numbers)
print("Prime Numbers in the List:", primes)