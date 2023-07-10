# ToDo: random population
# Also consider the fact: 1 Initialise the population 𝑃 with 𝜇 spanning trees such that
# 𝑐(𝑇) ≤ (1 + 𝛼) · OPT for all 𝑇 ∈ 𝑃.

def random_pop(mu, n, alpha):
    pass


# ToDo: seeded population
def seeded_pop(mu, n, alpha):
    pass


def all_ones_pop(mu, n, alpha):
    pop = []
    for i in range(mu):
        pop.append([1] * n)

    return pop