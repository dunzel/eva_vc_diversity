# The function head needs to be: def random_pop(mu, n, alpha, OPT, adjacency_matrix)
# mu is the number of individuals
# n is the number of genes
# alpha is the approximation factor
# OPT is the cost (size of vertex cover) of the optimal solution
# adjacency_matrix is the adjacency matrix of the graph
# mvc_ind is the minimum vertex cover as an individual
# The function needs to return a list of lists of 0s and 1s
import copy

import numpy as np

from eva_algos.utils import C, repair_ind


def heuristic_pop(mu, n, alpha, OPT, adjacency_matrix, mvc_ind):
    """
    Uses probabilistic 2-opt heuristic
    In expectation, the resulting population is a 2-approximation of the optimal solution
    So we can work with this when using the approximation factor up to alpha = 1
    """
    init_ind = None
    constrained = OPT < np.inf

    while True:
        zero_ind = [0] * n
        init_ind = repair_ind(zero_ind, adjacency_matrix, constrained)

        if C(init_ind, constrained, adjacency_matrix) <= (1 + alpha) * OPT:
            break

    P = [init_ind] * mu

    return copy.deepcopy(P)


def all_mvc_pop(mu, n, alpha, OPT, adjacency_matrix, mvc_ind):
    """
    Just returns the optimal solution mu times
    """
    return copy.deepcopy([mvc_ind] * mu)


def all_ones_pop(mu, n, alpha, OPT, adjacency_matrix, mvc_ind):
    """
    Creates a population of mu individuals with n genes, all set to 1
    WARNING: usage of this initial population generator is not recommended with the usage of CONSTRAINED = True
    The reason is that all offsprings after the mutation won't be in the allowed search space
    """
    P = []
    for i in range(mu):
        P.append([1] * n)

    return copy.deepcopy(P)
