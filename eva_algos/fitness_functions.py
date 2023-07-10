import numpy as np

# ToDo: diversity function
def diversity_func(population):
    pass


# ToDo: fitness function for unconstrained case
def fitness_func(ga_instance, solution, solution_idx, population):
    fitness = len(ga_instance.population) * len(solution)
    for individual in ga_instance.population:
        for i in range(len(solution)):
            if solution[i] != individual[i]:
                fitness = fitness + 1
    return fitness


# ToDo: fitness function for constrained case
def fitness_func_diversity(ga_instance, solution, solution_idx, population):
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


def mvc_optimal_fitness(ind, population):
    fitness = len(ind) - np.sum(ind)
    return fitness


def node_overlap(ind1, ind2):
    # not a good idea:
    # tends to set every individual to list of 0s
    VC_set_1 = set(i for i, x in enumerate(ind1) if x == 1)
    VC_set_2 = set(i for i, x in enumerate(ind2) if x == 1)
    return len(VC_set_1 & VC_set_2)


def hamming_distance(ind1, ind2):
    return sum(el1 != el2 for el1, el2 in zip(ind1, ind2))


def mvc_hamming_diversity(ind, population):
    # Copy the population and remove the individual from the population
    population = [i for i in population if i != ind]

    # calculate the diversity of the remaining population
    diversity = 0
    for i in population:
        for j in population:
            if i != j:
                diversity += hamming_distance(i, j)

    return diversity
