import matplotlib.pyplot as plt

# Global counters for recursive calls
dynamic_fibonacci_counter = 0
recursion_fibonacci_counter = 0

def dynamic_fibonacci(n, memo={}):
    global dynamic_fibonacci_counter  # Access the global counter   

    # Increment the counter for each recursive call
    dynamic_fibonacci_counter += 1
    
    # Base cases
    if n <= 1:
        return n
    
    # Check if the result is already computed
    if n in memo:
        return memo[n]
    
    # Recursively compute Fibonacci and store the result
    memo[n] = dynamic_fibonacci(n-1, memo) + dynamic_fibonacci(n-2, memo)
    
    return memo[n]

def recursion_fibonacci(n):
    global recursion_fibonacci_counter

    recursion_fibonacci_counter += 1

    if n <= 1:
        return n
    
    return recursion_fibonacci(n-1) + recursion_fibonacci(n-2)

# Collect data for plotting
n_values = range(1, 11)  # We will plot for n = 1 to 20
dynamic_counts = []
recursion_counts = []

for n in n_values:
    dynamic_fibonacci_counter = 0  # Reset the counter before each run
    recursion_fibonacci_counter = 0  # Reset the counter before each run
    dynamic_fibonacci_memo = {}  # Reset the memoization cache for each run

    # Calculate the dynamic Fibonacci and record the number of calls
    dynamic_fibonacci(n, memo=dynamic_fibonacci_memo)
    dynamic_counts.append(dynamic_fibonacci_counter)

    # Calculate the recursive Fibonacci and record the number of calls
    recursion_fibonacci(n)
    recursion_counts.append(recursion_fibonacci_counter)

# Plotting the results
plt.figure(figsize=(10, 5))
plt.plot(n_values, dynamic_counts, label="Dynamic Fibonacci", color='b', marker='o')
plt.plot(n_values, recursion_counts, label="Normal Recursion", color='r', marker='x')

plt.title("Comparison of Recursive Calls: Dynamic vs Normal Fibonacci")
plt.xlabel("Fibonacci n")
plt.ylabel("Number of Recursive Calls")
plt.legend()
plt.grid(True)
plt.show()
