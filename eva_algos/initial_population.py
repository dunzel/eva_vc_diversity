# The function head needs to be: def random_pop(mu, n, alpha, OPT, adjacency_matrix)
# mu is the number of individuals
# n is the number of genes
# alpha is the approximation factor
# OPT is the cost (size of vertex cover) of the optimal solution
# adjacency_matrix is the adjacency matrix of the graph
# mvc_ind is the minimum vertex cover as an individual
# The function needs to return a list of lists of 0s and 1s

def random_pop(mu, n, alpha, OPT, adjacency_matrix, mvc_ind):
    # ToDo: random population
    # Also consider the fact: 1 Initialise the population 𝑃 with 𝜇 spanning trees such that
    # 𝑐(𝑇) ≤ (1 + 𝛼) · OPT for all 𝑇 ∈ 𝑃.
    pass


# ToDo: seeded population
def heuristic_pop(mu, n, alpha, OPT, adjacency_matrix, mvc_ind):
    """
    Uses two heuristics to create a population of mu individuals with n genes
    """
    pass


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
    pop = []
    for i in range(mu):
        pop.append([1] * n)

    return pop
