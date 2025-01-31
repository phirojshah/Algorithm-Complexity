from itertools import combinations

def knapsack_bruteforce(weights, values, W):
    n = len(weights)
    max_value = 0
    best_subset = []

    # Generate all possible subsets of items (using combinations)
    for r in range(n + 1):  # from 0 to n items
        for subset in combinations(range(n), r):  # subsets of size r
            total_weight = sum(weights[i] for i in subset)
            total_value = sum(values[i] for i in subset)

            # If the subset's total weight is less than or equal to W, check the value
            if total_weight <= W and total_value > max_value:
                max_value = total_value
                best_subset = subset

    return max_value, best_subset

weights = [2, 3, 4, 5, 9, 7, 8, 6, 1, 10]
values = [3, 4, 5, 8, 7, 6, 9, 4, 3, 10]
W = 15

max_value, best_subset = knapsack_bruteforce(weights, values, W)
print("Maximum value:", max_value)
print("Best subset of items:", best_subset)
