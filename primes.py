"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("Numbers should be a positive integer greater than zero")
    list = []
    n= 2
    while len(list) < number_of_primes:
        if isPrime(n):
            list.append(n)
        n +=1
    return list



def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True