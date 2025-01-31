import random
import time
import matplotlib.pyplot as plt

# Sorting Algorithms Implementations
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L, R = arr[:mid], arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_inplace(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_inplace(arr, low, pi - 1)
        quick_sort_inplace(arr, pi + 1, high)
    return arr

def quick_sort(arr):
    quick_sort_inplace(arr, 0, len(arr) - 1)
    return arr

# Time Measurement and Plotting
algorithms = [
    (bubble_sort, 'Bubble Sort'),
    (insertion_sort, 'Insertion Sort'),
    (selection_sort, 'Selection Sort'),
    (heap_sort, 'Heap Sort'),
    (merge_sort, 'Merge Sort'),
    (quick_sort, 'Quick Sort')
]

sizes = [100, 200, 500, 1000, 2000]  # Adjust based on testing speed
timings = {name: [] for _, name in algorithms}

for size in sizes:
    arr = [random.randint(0, 10000) for _ in range(size)]
    print(f"Testing size: {size}")
    for sort_func, name in algorithms:
        total_time = 0.0
        runs = 3  # Average over 3 runs
        for _ in range(runs):
            start_time = time.time()
            sort_func(arr.copy())
            total_time += time.time() - start_time
        avg_time = total_time / runs
        timings[name].append(avg_time)
        print(f"  {name}: {avg_time:.5f} seconds")

# Plotting
plt.figure(figsize=(12, 8))
for name in timings:
    plt.plot(sizes, timings[name], marker='o', label=name)

plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Comparison of Sorting Algorithms')
plt.legend()
plt.grid(True)
plt.show()
