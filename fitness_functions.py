import numpy as np

# ToDo: diversity function
def diversity_func(population):
    pass


# ToDo: fitness function for unconstrained case
def fitness_func(ga_instance, solution, solution_idx):
    pass


# ToDo: fitness function for constrained case
def fitness_func(ga_instance, solution, solution_idx):
    pass


def mvc_optimal_fitness(ga_instance, solution, solution_idx, n):
    return n - np.sum(solution)
