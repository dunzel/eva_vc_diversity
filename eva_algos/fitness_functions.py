# function head needs to be: def fitness_func(ind, population):
# ind is the individual for which the fitness is calculated
# population is the whole population
import numpy as np

from eva_algos.utils import get_unique_pop


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
    population = get_unique_pop(population)


    # calculate the diversity of the remaining population
    diversity = 0
    for i in population:
        for j in population:
            if i != j:
                diversity += hamming_distance(i, j)

    return diversity

###########################
# Other fitness functions #
###########################


def node_overlap(ind1, ind2):
    """
    Calculates the node overlap (shared vc nodes) between two individuals
    """
    VC_set_1 = set(i for i, x in enumerate(ind1) if x == 1)
    VC_set_2 = set(i for i, x in enumerate(ind2) if x == 1)
    overlap = len(VC_set_1 & VC_set_2)
    return overlap


def node_overlap_ind_to_pop(index, population):
    """
    Calculates the average node overlap between an individual and the rest of the population
    """
    ind = population[index]
    pop_without_ind = population[:index] + population[index + 1:]

    overlap = 0
    for i in pop_without_ind:
        overlap += node_overlap(ind, i)

    overlap /= len(pop_without_ind)

    return overlap


def node_overlap_pop_mean_std(population, pool):
    """
    Calculates the mean and std of the node overlap of the population
    """
    if pool:
        overlaps = pool.starmap(node_overlap_ind_to_pop, [(i, population) for i in range(len(population))])

        mean = sum(overlaps) / len(overlaps)
        std = ((sum((x - mean) ** 2 for x in overlaps)) / len(overlaps)) ** 0.5
    else:
        mean = 0
        for i in population:
            mean += node_overlap_ind_to_pop(i, population)
        mean /= len(population)

        std = 0
        for i in population:
            std += (node_overlap_ind_to_pop(i, population) - mean) ** 2
        std /= len(population)
        std = std ** 0.5

    return round(mean, 2), round(std, 2)


def node_degree_and_leaf_pop_avg(population, adjacency_matrix):
    """
    Calculates the average node degree and average number of leafes in the population
    """
    avg_degree = 0
    avg_leafes = 0

    for ind in population:
        cum_degree = 0
        cum_leafes = 0
        for i in range(len(ind)):
            if ind[i] == 1:
                curr_node_degree = sum(adjacency_matrix[i])
                curr_node_degree -= adjacency_matrix[i][i] # remove weights as they are encoded in the adjacency matrix diagonal
                cum_degree += curr_node_degree

                if curr_node_degree == 1:
                    cum_leafes += 1

        avg_leafes += cum_leafes / sum(ind)
        avg_degree += cum_degree / sum(ind)

    avg_leafes /= len(population)
    avg_degree /= len(population)

    return round(avg_degree, 2), round(avg_leafes, 2)


