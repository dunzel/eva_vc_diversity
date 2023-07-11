import random
import numpy as np

from eva_algos.operators import get_vertex_nodes_idx, C
from settings import NUM_GENERATIONS, MU, ALPHA, GRAPH_INSTANCE, POPULATION_GENERATOR, \
    FITNESS_FX, MUTATION_FX, NUM_GENES, EARLY_DIVERSE_STOP, CONSTRAINED
from mvc_solver import ilp_solve_mvc


def mu_plus_one_ea():
    """
    Diversity maximising (𝜇 + 1)-EA
    :return: the diverse population, the so far best individual, the so far best vertex cover, the minimum vertex cover
    """
    min_vc = ilp_solve_mvc(GRAPH_INSTANCE)
    OPT = C(min_vc) if CONSTRAINED else np.Inf
    P = POPULATION_GENERATOR(MU, NUM_GENES, ALPHA, OPT)

    for i in range(NUM_GENERATIONS):
        # Choose a random individual from the population and mutate it
        T = random.choice(P)
        T_m = MUTATION_FX(T, GRAPH_INSTANCE)

        # Check if the cost of the mutated individual is in the range of the relaxed optimal solution
        if C(T_m) <= (1 + ALPHA) * OPT:
            P.append(T_m)

        # Remove the individual with the lowest fitness from the population
        # e.g. the lowest contribution to diversity
        if len(P) == MU + 1:
            worst_ind = min(P, key=lambda ind: FITNESS_FX(ind, P))
            P.remove(worst_ind)

        # Early stopping
        if EARLY_DIVERSE_STOP:
            # stops if all individuals in the population are different
            # counts the number of unique individuals in the population
            print(len(set(tuple(ind) for ind in P)))
            if len(set(tuple(ind) for ind in P)) == len(P):
                print(f"Early stopping at generation: {i}")
                break

    best_ind = max(P, key=lambda ind: FITNESS_FX(ind, P))  # only useful for minimum vertex cover search
    best_found_vc = get_vertex_nodes_idx(best_ind)

    return P, best_ind, best_found_vc, min_vc
