import random
import time
import matplotlib.pyplot as plt
import os

def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

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
    insertion_sort(data)
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
plt.title('Insertion Sort Time Complexity')
plt.grid(True)
plt.show()
