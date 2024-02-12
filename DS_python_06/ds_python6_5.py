n = int(input("Введите число: "))

def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)  

fact_n = factorial(n)

def decompose_factorial(n):
    #array of naturals numbers filled with zero in the beginning
    array_numbers = []
    for i in range(int(n**(1/2))):
        array_numbers.append(0)
        
    sqrt_n = int(n**(1/2))

    #filling array of naturals numbers with their factors
    #zero ones are prime
    for i in range(2, sqrt_n):
        for j in range(i * 2, sqrt_n, i):
            array_numbers[j] += 1

    #filling array with only primes
    array_primes = []
    for i in range(2, sqrt_n):
        if array_numbers[i] == 0:
            array_primes.append([i, 0])

    for i in range(len(array_primes)):
        while n > 0 and n % array_primes[i][0] == 0:
            array_primes[i][1] += 1
            n = n // array_primes[i][0]
    return array_primes

array_primes = decompose_factorial(fact_n)

print(f"{n}! = ", end="")
for i in range(len(array_primes)):
    if array_primes[i][1] != 0:
        print(f"{array_primes[i][0]}^{array_primes[i][1]} * ", end="")


        
    

    