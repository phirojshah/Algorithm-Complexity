import random
import time
import matplotlib.pyplot as plt
import os

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

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
plt.title(f'Merge Sort Time Complexity (Average of {num_runs} Runs)')
plt.grid(True)
plt.show()
