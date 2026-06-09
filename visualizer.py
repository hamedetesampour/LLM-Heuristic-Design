import matplotlib.pyplot as plt
import numpy as np

def plot_route(cities: np.ndarray, route: list[int], title: str, filename: str):
    """
    Generates a 2D plot of the TSP route and saves it to the disk.
    """
    plt.figure(figsize=(8, 6))
    
    # Order the coordinates according to the route, plus return to start
    ordered_cities = cities[route + [route[0]]]
    
    # Plot the lines and nodes
    plt.plot(ordered_cities[:, 0], ordered_cities[:, 1], marker='o', linestyle='-', color='#2c3e50', linewidth=2, markersize=8)
    
    # Highlight the starting node in red
    plt.plot(ordered_cities[0, 0], ordered_cities[0, 1], marker='s', color='#e74c3c', markersize=10, label="Start Node")
    
    # Annotate node indices for clarity
    for idx, (x, y) in enumerate(cities):
        plt.text(x + 1.5, y + 1.5, str(idx), fontsize=10, fontweight='bold', color='#34495e')

    plt.title(title, fontsize=14, pad=15)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    
    # Save the output image
    plt.savefig(filename, dpi=300)
    print(f"Saved visualization: {filename}")
    plt.close()