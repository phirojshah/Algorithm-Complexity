import random
import time
import matplotlib.pyplot as plt
import os

def merge_sort(arr):
    if len(arr) > 1:
        # Finding the middle of the list
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Recursively sorting both halves
        merge_sort(left_half)
        merge_sort(right_half)
        
        # Merging the sorted halves
        i = j = k = 0
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

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
    merge_sort(data)
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
plt.title('Merge Sort Time Complexity')
plt.grid(True)
plt.show()
