import random
import time
import matplotlib.pyplot as plt
import os

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

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
    selection_sort(data)
    end_time = time.time()
    return end_time - start_time

# Define the sizes of the lists and corresponding filenames
sizes = [1000, 2000, 3000, 4000]
file_names = [f"random_list_{size}.txt" for size in sizes]
times = []

# Generate and save lists to files if they do not already exist
for size, file_name in zip(sizes, file_names):
    if not os.path.exists(file_name):
        print(f"Generating and saving list of size {size} to {file_name}...")
        random_list = generate_random_list(size)
        save_list_to_file(random_list, file_name)
    else:
        print(f"File {file_name} already exists. Skipping generation.")

# Measure the time taken to sort lists of different sizes
for size, file_name in zip(sizes, file_names):
    print(f"Sorting list from file {file_name}...")
    elapsed_time = measure_time_for_sorting(file_name)
    times.append(elapsed_time)
    print(f"Time taken: {elapsed_time:.4f} seconds")

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(sizes, times, marker='o')
plt.xlabel('List Size')
plt.ylabel('Time Taken (seconds)')
plt.title('Selection Sort Time Complexity')
plt.grid(True)
plt.show()
