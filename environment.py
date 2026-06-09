import numpy as np

class TSPEnvironment:
    def __init__(self, num_cities: int = 10, seed: int = 42):
        """
        Initializes the TSP environment with reproducible random coordinates.
        Coordinates are bounded in a 100x100 2D space.
        """
        np.random.seed(seed)
        self.num_cities = num_cities
        self.cities = np.random.uniform(0, 100, size=(num_cities, 2))

    def calculate_distance(self, route: list[int]) -> float:
        """
        Calculates the exact Euclidean distance of a proposed route.
        """
        # Validate route integrity
        if len(route) != self.num_cities or set(route) != set(range(self.num_cities)):
            raise ValueError("Invalid sequence: The route must contain each city index exactly once.")

        dist = 0.0
        # Sum distances between consecutive nodes
        for i in range(self.num_cities - 1):
            p1 = self.cities[route[i]]
            p2 = self.cities[route[i+1]]
            dist += np.linalg.norm(p1 - p2)

        # Close the loop (return to the origin node)
        p_last = self.cities[route[-1]]
        p_first = self.cities[route[0]]
        dist += np.linalg.norm(p_last - p_first)

        return dist
        