import time
import random
import matplotlib.pyplot as plt
import numpy as np


def activity_selection(activities):
    activities.sort(key=lambda x: x[1])
    selected = [activities[0]]
    last_end = activities[0][1]
    
    for i in range(1, len(activities)):
        if activities[i][0] >= last_end:
            selected.append(activities[i])
            last_end = activities[i][1]
    return selected

# Measure time for different sizes
sizes = [10, 50, 100, 500, 1000, 5000, 10000]
times = {"Greedy": []}

for size in sizes:
    activities = [(random.randint(0, 10000), random.randint(0, 10000)) for _ in range(size)]
    activities = [(s, e) if s < e else (e, s) for s, e in activities]
    
    # Greedy
    start = time.time()
    activity_selection(activities)
    end = time.time()
    times["Greedy"].append(end - start)

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(sizes, times["Greedy"], marker='o', label="Greedy Activity Selection")
plt.xlabel("Number of Activities")
plt.ylabel("Time (seconds)")
plt.title("Greedy Activity Selection Performance")
plt.legend()
plt.grid()
plt.show()
