import random
import time
import os
from environment import TSPEnvironment
from llm_agent import get_llm_mutation
from visualizer import plot_route

def run_evolution(generations: int = 10, num_cities: int = 10):
    # 1. Create a directory to hold the sequence of images
    output_dir = "visualizations"
    os.makedirs(output_dir, exist_ok=True)
    
    env = TSPEnvironment(num_cities=num_cities, seed=42)
    current_route = list(range(env.num_cities))
    random.shuffle(current_route)
    best_distance = env.calculate_distance(current_route)
    
    print(f"--- Initialization ---")
    print(f"Initial Route: {current_route}")
    print(f"Initial Distance: {best_distance:.2f}\n")

    # Save the initial state as frame 00
    plot_route(env.cities, current_route, f"Initial State (Distance: {best_distance:.2f})", f"{output_dir}/gen_00.png")

    coords_list = env.cities.tolist()

    for gen in range(1, generations + 1):
        print(f"--- Generation {gen} ---")
        
        mutated_route = get_llm_mutation(current_route, best_distance, coords_list)
        new_distance = env.calculate_distance(mutated_route)
        
        if new_distance < best_distance:
            print(f"[SUCCESS] LLM mutation improved distance: {best_distance:.2f} -> {new_distance:.2f}")
            current_route = mutated_route
            best_distance = new_distance
        elif mutated_route == current_route:
            print("[STAGNATION] LLM returned identical sequence or failed validation.")
        else:
            print(f"[REJECTED] LLM mutation increased distance to {new_distance:.2f}.")
            
        print(f"Current Best Route: {current_route}\n")
        
        # 2. Save the visualization for THIS generation
        # The :02d formats the number with a leading zero (gen_01.png, gen_02.png) for clean sorting
        plot_route(env.cities, current_route, f"Generation {gen} (Distance: {best_distance:.2f})", f"{output_dir}/gen_{gen:02d}.png")
        
        time.sleep(5) 

    return current_route, best_distance

if __name__ == "__main__":
    print("Starting LLM-Guided Evolutionary Search...\n")
    final_route, final_dist = run_evolution(generations=10, num_cities=10)
    print("========================================")
    print(f"Final Optimized Sequence: {final_route}")
    print(f"Final Minimum Distance: {final_dist:.2f}")
    print("All generation frames have been saved to the /visualizations folder.")