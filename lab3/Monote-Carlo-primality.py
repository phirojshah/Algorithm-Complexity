import random
import time
import matplotlib.pyplot as plt

# Fermat Primality Test
def fermat_primality_test(n, k=5):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    
    # Perform the test k times
    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False  # n is definitely composite
    return True  # n is probably prime

# Miller-Rabin Primality Test
def miller_rabin_primality_test(n, k=5):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    
    # Write n-1 as d * 2^r
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # Perform the test k times
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False  # n is definitely composite
    return True  # n is probably prime

# Function to time the tests and collect results
def compare_primality_tests(n_values, k= 20):
    fermat_times = []
    miller_rabin_times = []

    for n in n_values:
        # Time Fermat Test
        start_time = time.time()
        fermat_primality_test(n, k)
        fermat_times.append(time.time() - start_time)

        # Time Miller-Rabin Test
        start_time = time.time()
        miller_rabin_primality_test(n, k)
        miller_rabin_times.append(time.time() - start_time)

    return n_values, fermat_times, miller_rabin_times

# Adjusting the n_values to larger numbers for better comparison
n_values = [7, 13, 23, 47, 91, 95, 97]

# Time the tests
n_values, fermat_times, miller_rabin_times = compare_primality_tests(n_values)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(n_values, fermat_times, label="Fermat Primality Test", color='b', linestyle='-', linewidth=2)  # Line for Fermat
plt.plot(n_values, miller_rabin_times, label="Miller-Rabin Primality Test", color='r', linestyle='-', linewidth=2)  # Line for Miller-Rabin

plt.title("Comparison of Primality Tests: Fermat vs Miller-Rabin")
plt.xlabel("Number n")
plt.ylabel("Time (seconds)")
plt.legend()
plt.grid(True)
plt.show()


