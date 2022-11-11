"""
Project Euler: Problem 3

"The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"

First we must construct a list of prime numbers up to the square root of 600851475143
"""

import math

num = 600851475143
root = math.ceil(math.sqrt(num))
primes = [2]

for i in range(2, root):
    for j in range(len(primes)):
        if i % primes[j] != 0:
            counter = 1
        else:
            counter = 0
            break
    if counter == 1:
        primes.append(i)

for item in reversed(primes):
    if num % item == 0:
        print(item)
        break
    else:
        continue