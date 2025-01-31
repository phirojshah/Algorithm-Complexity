import itertools
import time
import random
import numpy as np

def generate_random_distance_matrix(num_cities, min_distance=10, max_distance=100, seed=None):
    """
    Generate a symmetric random distance matrix.
    
    Args:
    - num_cities: Number of cities
    - min_distance: Minimum distance between cities
    - max_distance: Maximum distance between cities
    - seed: Random seed for reproducibility
    
    Returns:
    - Symmetric distance matrix
    """
    if seed is not None:
        random.seed(seed)
        np.random.seed(seed)
    
    # Create a symmetric distance matrix
    matrix = np.zeros((num_cities, num_cities), dtype=int)
    
    for i in range(num_cities):
        for j in range(i+1, num_cities):
            # Random distance, ensuring no self-distance
            distance = random.randint(min_distance, max_distance)
            matrix[i][j] = distance
            matrix[j][i] = distance
    
    return matrix.tolist()

def calculate_total_distance(route, distance_matrix):
    """Calculate total distance for a given route."""
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i]][route[i+1]]
    total_distance += distance_matrix[route[-1]][route[0]]  # Return to start
    return total_distance

def brute_force_tsp(distance_matrix):
    """
    Solve Traveling Salesman Problem using brute force.
    Tries all possible permutations to find shortest route.
    """
    num_cities = len(distance_matrix)
    
    cities = list(range(num_cities))
    all_routes = list(itertools.permutations(cities[1:]))
    
    shortest_route = [0] + list(all_routes[0])
    shortest_distance = calculate_total_distance(shortest_route, distance_matrix)
    
    for route_cities in all_routes:
        current_route = [0] + list(route_cities)
        current_distance = calculate_total_distance(current_route, distance_matrix)
        
        if current_distance < shortest_distance:
            shortest_route = current_route
            shortest_distance = current_distance
    
    return shortest_route, shortest_distance

def main():
    # Number of cities (be careful with large numbers!)
    num_cities = 10
    
    # Generate random distance matrix
    distance_matrix = generate_random_distance_matrix(num_cities, seed=42)
    
    print(f"Distance Matrix for {num_cities} cities:")
    for row in distance_matrix:
        print(row)
    
    start_time = time.time()
    best_route, best_distance = brute_force_tsp(distance_matrix)
    end_time = time.time()
    
    print(f"\nBest Route: {best_route}")
    print(f"Total Distance: {best_distance}")
    print(f"Computation Time: {end_time - start_time:.4f} seconds")

if __name__ == '__main__':
    main()