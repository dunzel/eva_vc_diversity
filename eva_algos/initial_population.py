# The function head needs to be: def random_pop(mu, n, alpha, OPT, adjacency_matrix)
# mu is the number of individuals
# n is the number of genes
# alpha is the approximation factor
# OPT is the cost (size of vertex cover) of the optimal solution
# adjacency_matrix is the adjacency matrix of the graph
# mvc_ind is the minimum vertex cover as an individual
# The function needs to return a list of lists of 0s and 1s
from eva_algos.operators import repair_ind, C


def random_pop(mu, n, alpha, OPT, adjacency_matrix, mvc_ind):
    # random population
    # Also consider the fact: 1 Initialise the population 𝑃 with 𝜇 spanning trees such that
    # 𝑐(𝑇) ≤ (1 + 𝛼) · OPT for all 𝑇 ∈ 𝑃.
    pass


def heuristic_pop(mu, n, alpha, OPT, adjacency_matrix, mvc_ind):
    """
    Uses probabilistic 2-opt heuristic
    """
    P = []
    for _ in range(mu):
        zero_ind = [0] * n
        repaired_ind = repair_ind(zero_ind, adjacency_matrix)

        assert C(repaired_ind) <= (1 + alpha) * OPT

        P.append(repaired_ind)

    return P



def all_mvc_pop(mu, n, alpha, OPT, adjacency_matrix, mvc_ind):
    """
    Just returns the optimal solution mu times
    """
    return [mvc_ind] * mu


def all_ones_pop(mu, n, alpha, OPT, adjacency_matrix, mvc_ind):
    """
    Creates a population of mu individuals with n genes, all set to 1
    WARNING: usage of this initial population generator is not recommended with the usage of CONSTRAINED = True
    """
    P = []
    for i in range(mu):
        P.append([1] * n)

    return P
