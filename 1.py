"""
Project Euler: Problem 1

"If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000."

Sum of all multiples of 3 and 5 below 1k = sum of multiples of 3 below 1k + sum of multiples of 5 below 1k - sum of multiples of 15 below 1k

"""
import math

def multi_sum(a):

    return sum(a*x for x in range(math.ceil(1000/a)))

sumthrees = multi_sum(3)
sumfives = multi_sum(5)
sumcommon = multi_sum(15)

print(sumthrees + sumfives - sumcommon)

"""
I'm not sure if this approach makes a real difference when compared to iterating over all integers from 1 to 999 given the size of the problem.
The code yields the correct answer and the code runs fast enough in either case, so I will leave this solution as is.
"""
