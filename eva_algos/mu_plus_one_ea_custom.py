import random
import numpy as np

from general_settings import NUM_GENERATIONS, MU, ALPHA, GRAPH_INSTANCE, POPULATION_GENERATOR, \
    FITNESS_FX, MUTATION_FX
from mvc_solver import ilp_solve_mvc


def C(ind):
    """Cost function"""
    return sum(ind)


def mu_plus_one_ea(constrained=False):
    """
    Diversity maximising (𝜇 + 1)-EA
    """
    OPT = C(ilp_solve_mvc(GRAPH_INSTANCE)) if constrained else np.Inf
    P = POPULATION_GENERATOR(MU, NUM_GENERATIONS, ALPHA)

    for i in range(NUM_GENERATIONS):
        # Choose a random individual from the population and mutate it
        T = random.choice(P)
        T_m = MUTATION_FX(T)

        # Check if the cost of the mutated individual is in the range of the relaxed optimal solution
        if C(T_m) <= (1 + ALPHA) * OPT:
            P.append(T_m)

        # Remove the individual with the lowest fitness from the population
        # e.g. the lowest contribution to diversity
        if len(P) == MU + 1:
            P.remove(min(P, key=lambda x: FITNESS_FX(x)))

    return P
