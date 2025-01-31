import random
import time
import matplotlib.pyplot as plt

# Generate random activities with start and finish times
def generate_random_activities(n):
    activities = []
    for i in range(n):
        start = random.randint(0, 10 * n)
        finish = random.randint(start + 1, 10 * n + 10)
        activities.append((start, finish))
    # Sort activities based on finish time
    activities.sort(key=lambda x: x[1])
    return activities

# Brute Force Approach (Exponential Time Complexity)
def brute_force_activity_selection(activities):
    n = len(activities)
    best_solution = []
    # Iterate through all subsets of activities
    for i in range(1 << n):
        selected_activities = []
        for j in range(n):
            if i & (1 << j):
                selected_activities.append(activities[j])
        # Check if the selected activities are compatible
        if is_compatible(selected_activities):
            if len(selected_activities) > len(best_solution):
                best_solution = selected_activities
    return best_solution

# Greedy Approach (Optimal Solution with Sorting)
def greedy_activity_selection(activities):
    selected_activities = []
    last_finish_time = -1
    for activity in activities:
        if activity[0] >= last_finish_time:
            selected_activities.append(activity)
            last_finish_time = activity[1]
    return selected_activities

# Check if a set of activities are compatible
def is_compatible(activities):
    activities = sorted(activities, key=lambda x: x[1])  # Sort by finish time
    for i in range(1, len(activities)):
        if activities[i][0] < activities[i-1][1]:  # If start time of one activity is before finish time of the previous
            return False
    return True

# Measure the execution time of each algorithm
def measure_time(algorithm, activities):
    start_time = time.time()
    algorithm(activities)
    end_time = time.time()
    return end_time - start_time

# Main function to compare execution times of both algorithms
def compare_algorithms():
    n_values = list(range(10, 20))  # Input sizes from 4 to 10
    brute_force_times = []
    greedy_times = []
    
    for n in n_values:
        activities = generate_random_activities(n)
        
        # Measure time for brute force
        brute_force_time = measure_time(brute_force_activity_selection, activities)
        brute_force_times.append(brute_force_time)
        
        # Measure time for greedy algorithm
        greedy_time = measure_time(greedy_activity_selection, activities)
        greedy_times.append(greedy_time)
    
    # Plot the comparison of times for both algorithms
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, brute_force_times, label="Brute Force", color="red", marker='o')
    plt.plot(n_values, greedy_times, label="Greedy", color="blue", marker='x')
    plt.xlabel("Number of Activities (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Comparison of Activity Selection Algorithms")
    plt.legend()
    plt.grid(True)
    plt.show()

# Run the comparison
compare_algorithms()
