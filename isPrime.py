import time

def sieve(limit):
    primes = [True] * (limit + 1)
    primes[0], primes[1] = False, False  # 0 și 1 nu sunt prime
    
    for num in range(2, int(limit ** 0.5) + 1):
        if primes[num]:
            for multiple in range(num * num, limit + 1, num):
                primes[multiple] = False
                
    return [num for num, is_prime in enumerate(primes) if is_prime]

start_time = time.time()

primes = sieve(1000)

end_time = time.time()

print(primes)
print(f"Execution time: {end_time - start_time:.6f} seconds")
