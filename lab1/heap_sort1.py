import random
import time
import matplotlib.pyplot as plt
import os

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1     # left = 2*i + 1
    right = 2 * i + 2    # right = 2*i + 2

    # See if left child of root exists and is greater than root
    if left < n and arr[i] < arr[left]:
        largest = left

    # See if right child of root exists and is greater than root
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

def generate_random_list(size):
    return [random.randint(0, 10000) for _ in range(size)]

def save_list_to_file(lst, filename):
    with open(filename, 'w') as file:
        for item in lst:
            file.write(f"{item}\n")

def read_list_from_file(filename):
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file]

def measure_time_for_sorting(file_name):
    data = read_list_from_file(file_name)
    start_time = time.time()
    heap_sort(data)
    end_time = time.time()
    return end_time - start_time

def run_experiment(sizes, num_runs):
    avg_times = []
    for size in sizes:
        file_name = f"random_list_{size}.txt"
        if not os.path.exists(file_name):
            print(f"Generating and saving list of size {size} to {file_name}...")
            random_list = generate_random_list(size)
            save_list_to_file(random_list, file_name)
        else:
            print(f"File {file_name} already exists. Skipping generation.")
        
        times = []
        for _ in range(num_runs):
            print(f"Sorting list from file {file_name} (run {_ + 1})...")
            elapsed_time = measure_time_for_sorting(file_name)
            times.append(elapsed_time)
            print(f"Time taken: {elapsed_time:.4f} seconds")
        
        avg_time = sum(times) / num_runs
        avg_times.append(avg_time)
        print(f"Average time for list size {size}: {avg_time:.4f} seconds")
    
    return avg_times

# Define the sizes of the lists and number of runs
sizes = [1000, 2000, 3000, 4000]
num_runs = 30

# Run the experiment and get average times
avg_times = run_experiment(sizes, num_runs)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(sizes, avg_times, marker='o', linestyle='-', color='b')
plt.xlabel('List Size')
plt.ylabel('Average Time Taken (seconds)')
plt.title(f'Heap Sort Time Complexity (Average of {num_runs} Runs)')
plt.grid(True)
plt.show()
