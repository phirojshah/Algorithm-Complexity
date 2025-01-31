import itertools

def calculate_total_distance(cities, distance_matrix):
    # Calculate the total distance of the route
    total_distance = 0
    for i in range(len(cities) - 1):
        total_distance += distance_matrix[cities[i]][cities[i + 1]]
    total_distance += distance_matrix[cities[-1]][cities[0]]  # Return to the starting city
    return total_distance

def travelling_salesman_bruteforce(distance_matrix):
    n = len(distance_matrix)
    # Generate all possible permutations of the cities (excluding the starting city)
    cities = list(range(n))
    
    min_distance = float('inf')
    best_route = None
    
    for perm in itertools.permutations(cities[1:]):  # Fix the first city to avoid repetitive cycles
        route = [cities[0]] + list(perm)  # Start with the fixed city
        total_distance = calculate_total_distance(route, distance_matrix)
        
        if total_distance < min_distance:
            min_distance = total_distance
            best_route = route
    
    return best_route, min_distance

# Example usage:
distance_matrix = [
    [0, 10, 15, 20, 25],
    [10, 0, 15, 25, 30],
    [15, 35, 0, 30, 5],
    [20, 25, 30, 0, 10],
    [25, 30, 5, 10, 0]
]

best_route, min_distance = travelling_salesman_bruteforce(distance_matrix)
print(f"Best route: {best_route}")
print(f"Minimum distance: {min_distance}")
