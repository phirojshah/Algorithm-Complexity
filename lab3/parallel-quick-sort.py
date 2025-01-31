import random
import multiprocessing as mp
from typing import List, Any

def choose_pivot(arr: List[Any]) -> Any:
    """Randomly select a pivot from the array."""
    return random.choice(arr) if arr else None

def partition(arr: List[Any], pivot: Any) -> tuple:
    """
    Partition the array around the pivot.
    Returns: left, equal, right subarrays
    """
    left, equal, right = [], [], []
    
    for item in arr:
        if item < pivot:
            left.append(item)
        elif item == pivot:
            equal.append(item)
        else:
            right.append(item)
    
    return left, equal, right

def parallel_quicksort(arr: List[Any]) -> List[Any]:
    """
    Parallel quicksort implementation with recursive parallelism.
    """
    # Base cases
    if len(arr) <= 1:
        return arr
    
    # Choose pivot randomly
    pivot = choose_pivot(arr)
    
    # Partition the array
    left, equal, right = partition(arr, pivot)
    
    # Use ProcessPoolExecutor for more flexible parallelism
    with mp.Pool(processes=mp.cpu_count()) as pool:
        # Parallelize sorting of left and right subarrays
        try:
            sorted_subarrays = pool.map(
                parallel_quicksort, 
                [left, right]
            )
        except Exception as e:
            # Fallback to sequential sorting if parallelism fails
            sorted_subarrays = [
                sorted(left),
                sorted(right)
            ]
    
    # Combine results
    return sorted_subarrays[0] + equal + sorted_subarrays[1]

def main():
    """Demonstrate and test parallel quicksort"""
    import time
    
    # Generate large random list
    test_list = [random.randint(1, 10000) for _ in range(100_000_000)]
    
    # Parallel quicksort
    start_time = time.time()
    sorted_list = parallel_quicksort(test_list)
    parallel_time = time.time() - start_time
    print(f"Parallel Quicksort Time: {parallel_time:.4f} seconds")
    
    # Verify sorting
    assert sorted_list == sorted(test_list), "Sorting failed!"
    
    # Compare with built-in sort
    start_time = time.time()
    builtin_sorted = sorted(test_list)
    builtin_time = time.time() - start_time
    print(f"Built-in Sort Time: {builtin_time:.4f} seconds")
    
    def quick_sort_sequential(arr):
        if len(arr) <= 1:
            return arr
        pivot = random.choice(arr)
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort_sequential(left) + middle + quick_sort_sequential(right)
    
    start_time = time.time()
    sequenial_sorted = quick_sort_sequential(test_list)
    sequential_time = time.time() - start_time
    print(f"Sequential Sort Time: {sequential_time:.4f} seconds")

if __name__ == '__main__':
    # Ensure proper multiprocessing support on Windows
    mp.freeze_support()
    main()