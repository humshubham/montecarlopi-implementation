import multiprocessing
import random
import math
from time import time

class MonteCarloPi:
    def __init__(self, total_points, num_processes):
        """
        Initialize the MonteCarloPi simulation.

        Args:
            total_points (int): Total number of points to generate.
            num_processes (int): Number of processes to use.
        """
        self.total_points = total_points
        self.num_processes = num_processes

    def _simulate(self, points):
        """
        Simulate a Monte Carlo run for a subset of points.

        Args:
            points (int): Number of points for this process.

        Returns:
            int: Number of points inside the unit circle.
        """
        inside_circle = 0
        for _ in range(points):
            x, y = random.random(), random.random()
            if math.sqrt(x**2 + y**2) <= 1:
                inside_circle += 1
        return inside_circle

    def estimate_pi(self):
        """
        Estimate the value of π using multiprocessing.

        Returns:
            float: Estimated value of π.
        """
        points_per_process = self.total_points // self.num_processes
        pool = multiprocessing.Pool(processes=self.num_processes)
        
        # Divide the work among processes
        results = pool.map(self._simulate, [points_per_process] * self.num_processes)
        pool.close()
        pool.join()
        
        # Combine results
        total_inside_circle = sum(results)
        return (4 * total_inside_circle) / self.total_points

if __name__ == "__main__":
    total_points = 1_000_000
    num_processes = 4

    monte_carlo = MonteCarloPi(total_points, num_processes)
    start_time = time()
    pi_estimate = monte_carlo.estimate_pi()
    end_time = time()

    print(f"Estimated π (Multiprocessing): {pi_estimate}")
    print(f"Execution Time: {end_time - start_time:.4f} seconds")

