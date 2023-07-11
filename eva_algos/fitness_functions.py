import numpy as np

##############################
# New fitness function ideas #
##############################

# function head needs to be: def fitness_func(ind, population):
# ind is the individual for which the fitness is calculated
# population is the whole population


def mvc_optimal_fitness(ind, population):
    """
    An optimal fitness function for the MVC problem
    an individual is fitter the smaller the vertex cover is
    :param ind: binary list
    :param population: list of binary lists
    :return: number of vertices that are NOT in the vertex cover
    """
    fitness = len(ind) - np.sum(ind)
    return fitness


def hamming_distance(ind1, ind2):
    """
    Calculates the hamming distance between two individuals
    :param ind1: binary list
    :param ind2: binary list
    :return:
    """
    return sum(el1 != el2 for el1, el2 in zip(ind1, ind2))


def mvc_hamming_diversity(ind, population):
    """
    Calculates the hamming diversity of all pairs of individuals in the population without the individual ind
    :param ind: binary list
    :param population: list of binary lists
    :return: summed hamming diversity
    """

    # Copy the population and remove the individual from the population
    population = [i for i in population if i != ind]

    # calculate the diversity of the remaining population
    diversity = 0
    for i in population:
        for j in population:
            if i != j:
                diversity += hamming_distance(i, j)

    return diversity

##############################
# Old fitness function ideas #
##############################


def fitness_func(ga_instance, solution, solution_idx, population):
    fitness = len(ga_instance.population) * len(solution)
    for individual in ga_instance.population:
        for i in range(len(solution)):
            if solution[i] != individual[i]:
                fitness = fitness + 1
    return fitness


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