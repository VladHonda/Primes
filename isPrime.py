import time

nums = range(1, 1000)

def isPrime(num):
    if num < 2:
        return False
    for x in range(2, int(num ** 0.5) + 1):  # Optimizare: verificăm doar până la rădăcina pătrată a numărului
        if num % x == 0:
            return False
    return True

start_time = time.time()

primes = list(filter(isPrime, nums))

end_time = time.time()

print(primes)
print(f"Execution time: {end_time - start_time:.6f} seconds")
