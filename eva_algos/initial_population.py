# The function head needs to be: def random_pop(mu, n, alpha)
# mu is the number of individuals
# n is the number of genes
# alpha is the approximation factor

def random_pop(mu, n, alpha):
    # ToDo: random population
    # Also consider the fact: 1 Initialise the population 𝑃 with 𝜇 spanning trees such that
    # 𝑐(𝑇) ≤ (1 + 𝛼) · OPT for all 𝑇 ∈ 𝑃.
    pass


# ToDo: seeded population
def seeded_pop(mu, n, alpha):
    pass


def all_ones_pop(mu, n, alpha):
    """
    Creates a population of mu individuals with n genes, all set to 1
    WARNING: usage of this initial population generator is not recommended with the usage of CONSTRAINED = True
    :param mu: number of individuals
    :param n: number of genes
    :param alpha: is ignored
    :return: list of lists of 1s
    """
    pop = []
    for i in range(mu):
        pop.append([1] * n)

    return pop
