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


def node_overlap(ind1, ind2):
    # not a good idea:
    # tends to set every individual to list of 0s
    VC_set_1 = set(i for i, x in enumerate(ind1) if x == 1)
    VC_set_2 = set(i for i, x in enumerate(ind2) if x == 1)
    return len(VC_set_1 & VC_set_2)


def hamming_distance(ind1, ind2):
    """
    Calculates the hamming distance between two individuals
    :param ind1: binary list
    :param ind2: binary list
    :return:
    """
    return sum(el1 != el2 for el1, el2 in zip(ind1, ind2))


def remove_first_instance(pop, ind):
    """
    Removes the first instance of ind from the population
    :param pop:
    :param ind:
    :return: the population without the first instance of ind
    """
    try:
        first_instance_index = next(i for i, x in enumerate(pop) if x == ind)
        return pop[:first_instance_index] + pop[first_instance_index + 1:]
    except StopIteration:
        return pop


def mvc_hamming_diversity(ind, population):
    """
    Calculates the hamming diversity of all pairs of individuals in the population without the individual ind
    :param ind: binary list
    :param population: list of binary lists
    :return: summed hamming diversity
    WARNING:    is inefficient for large populations... maybe we should use a different diversity measure
                or parallelize the calculation?
    """

    # Copy the population and remove the individual from the population
    if ind is not None:
        population = remove_first_instance(population.copy(), ind)

    # make all ind in the pop unique:
    population = set(tuple(i) for i in population)
    population = [list(x) for x in population]


    # calculate the diversity of the remaining population
    diversity = 0
    for i in population:
        for j in population:
            if i != j:
                diversity += hamming_distance(i, j)

    return diversity


def mvc_hamming_diversity_cmp(ind, population):
    # gets stuck in local optima because they have the same diversity rating as the optimal solution
    diversity = 0
    for i in population:
        if i != ind:
            diversity += hamming_distance(ind, i)

    return diversity
