import numpy as np

# ToDo: diversity function
def diversity_func(population):
    pass


# ToDo: fitness function for unconstrained case
def fitness_func(ga_instance, solution, solution_idx):
    fitness = len(ga_instance.population) * len(solution)
    for individual in ga_instance.population:
        for i in range(len(solution)):
            if solution[i] != individual[i]:
                fitness = fitness + 1
    return fitness


# ToDo: fitness function for constrained case
def fitness_func_diversity(ga_instance, solution, solution_idx):
    """
    Calculates the diversity by reducing it for every node in the solutions vertex cover
    """
    fitness = len(ga_instance.population) * len(solution)
    for individual in ga_instance.population:
        for i in range(len(solution)):
            if solution[i] == 1:
                if individual[i] == 1:
                    fitness = fitness - 1
    print("fitness: ", end="")
    print(fitness, end="")
    print(" for ", end="")
    print(solution)
    return fitness


def mvc_optimal_fitness(ga_instance, solution, solution_idx):
    fitness = len(solution) - np.sum(solution)
    #print("fitness: ", end="")
    #print(fitness, end="")
    #print(" for ", end="")
    #print(solution)
    return fitness
