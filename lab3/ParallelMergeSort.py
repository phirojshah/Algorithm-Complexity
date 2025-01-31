import random
import time
import multiprocessing
import matplotlib.pyplot as plt

# Merge function for Merge Sort
def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# Normal Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

# Parallel Merge Sort using multiprocessing
def parallel_merge_sort(arr, return_dict, index):
    if len(arr) <= 1:
        return_dict[index] = arr
        return

    mid = len(arr) // 2

    # Create manager dictionary to store results
    left_process = multiprocessing.Process(target=parallel_merge_sort_worker, args=(arr[:mid], return_dict, 2 * index))
    right_process = multiprocessing.Process(target=parallel_merge_sort_worker, args=(arr[mid:], return_dict, 2 * index + 1))

    left_process.start()
    right_process.start()

    left_process.join()
    right_process.join()

    # After processes are done, merge the results from return_dict
    left_result = return_dict.get(2 * index, [])
    right_result = return_dict.get(2 * index + 1, [])

    return_dict[index] = merge(left_result, right_result)

def parallel_merge_sort_worker(arr, return_dict, index):
    sorted_arr = merge_sort(arr)
    return_dict[index] = sorted_arr

# Measure execution time for Normal Merge Sort
def measure_normal_time(size):
    arr = [random.randint(0, 10000) for _ in range(size)]
    start_time = time.time()
    merge_sort(arr)
    return time.time() - start_time

# Measure execution time for Parallel Merge Sort
def measure_parallel_time(size):
    arr = [random.randint(0, 10000) for _ in range(size)]

    return_dict = multiprocessing.Manager().dict()  # Use a manager dict to store results
    start_time = time.time()
    parallel_merge_sort(arr, return_dict, 0)
    return time.time() - start_time

# List of input sizes
sizes = [100, 500, 1000, 5000]
normal_times = []
parallel_times = []

# Main block to run the script
if __name__ == '__main__':
    # Measure the execution times for both algorithms
    for size in sizes:
        normal_times.append(measure_normal_time(size))
        parallel_times.append(measure_parallel_time(size))

    # Plotting the execution times
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, normal_times, label="Normal Merge Sort", color='b', marker='o')
    plt.plot(sizes, parallel_times, label="Parallel Merge Sort", color='r', marker='x')

    plt.xlabel("Array Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Comparison of Normal and Parallel Merge Sort")
    plt.legend()
    plt.grid(True)
    plt.show()
