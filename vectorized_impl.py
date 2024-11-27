import numpy as np
from time import time

def estimate_pi_vectorized(total_points):
    """
    Estimate the value of π using vectorized operations with NumPy.

    Args:
        total_points (int): Total number of points to generate.

    Returns:
        float: Estimated value of π.
    """
    # Generate random points in the unit square
    x = np.random.random(total_points)
    y = np.random.random(total_points)

    # Calculate the distance from the origin
    distances = np.sqrt(x**2 + y**2)

    # Count points inside the unit circle
    inside_circle = np.sum(distances <= 1)

    return (4 * inside_circle) / total_points

if __name__ == "__main__":
    total_points = 1_000_000

    start_time = time()
    pi_estimate = estimate_pi_vectorized(total_points)
    end_time = time()

    print(f"Estimated π (Vectorized): {pi_estimate}")
    print(f"Execution Time: {end_time - start_time:.4f} seconds")

