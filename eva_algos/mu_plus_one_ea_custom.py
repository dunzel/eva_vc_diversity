import random
import numpy as np

from eva_algos.operators import get_vertex_nodes_idx, C, get_ind_from_vertex_nodes_idx, get_unique_pop, count_unique_pop
from settings import NUM_GENERATIONS, MU, ALPHA, GRAPH_INSTANCE, POPULATION_GENERATOR, \
    FITNESS_FX, MUTATION_FX, NUM_GENES, EARLY_DIVERSE_STOP, CONSTRAINED, EARLY_DIVERSE_STOP_CNT, DEBUG, \
    NO_FIT_IMP_STOP_CNT, RANDOM_SEED
from misc.mvc_solver import ilp_solve_mvc


def mu_plus_one_ea():
    """
    Diversity maximising (𝜇 + 1)-EA
    :return: the diverse population, the so far best individual, the so far best vertex cover, the minimum vertex cover
    """
    random.seed(RANDOM_SEED)

    min_vc = ilp_solve_mvc(GRAPH_INSTANCE)
    min_vc_ind = get_ind_from_vertex_nodes_idx(min_vc, NUM_GENES)
    OPT = C(min_vc_ind) if CONSTRAINED else np.Inf
    P = POPULATION_GENERATOR(MU, NUM_GENES, ALPHA, OPT, GRAPH_INSTANCE, min_vc_ind)

    if DEBUG:
        P = get_unique_pop(P)
        print("Heuristic population found {} individuals".format(len(P)))
        # for ind in P:
        #   vertex_cover_graph(GRAPH_INSTANCE, get_vertex_nodes_idx(ind))

    last_gen_diversity = 0
    same_diversity_cnt = 0

    last_gen_fitness = 0
    same_fitness_cnt = 0

    i = 0
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
            ind_fit_fx = lambda ind: FITNESS_FX(ind, P)
            # worst_fit = max(map(ind_fit, P))
            worst_ind = max(P, key=ind_fit_fx)
            P.remove(worst_ind)

        assert len(P) == MU

        # Check diversity
        different_ind_cnt = len(set(tuple(ind) for ind in P))
        print(f"Generation {i}: {different_ind_cnt} unique individuals")

        # Early stopping if maximum diversity is reached
        if EARLY_DIVERSE_STOP:
            # stops if all individuals in the population are different
            # counts the number of unique individuals in the population
            if different_ind_cnt == len(P):
                print(f"Early stopped reason: max diversity reached")
                break

        # Early stopping if no improvement in diversity for EARLY_DIVERSE_STOP_CNT generations
        if EARLY_DIVERSE_STOP_CNT > 0:
            if different_ind_cnt > last_gen_diversity:
                last_gen_diversity = different_ind_cnt
                same_diversity_cnt = 0
            else:
                same_diversity_cnt += 1

            if same_diversity_cnt == EARLY_DIVERSE_STOP_CNT:
                print(f"Early stopped reason: no improvement in diversity for {EARLY_DIVERSE_STOP_CNT} generations")
                break

        # Early stopping if no improvement in fitness for NO_FIT_IMP_STOP_CNT generations
        if NO_FIT_IMP_STOP_CNT > 0:
            curr_gen_fitness = FITNESS_FX(None, P)
            print(f"Generation {i}: fitness {curr_gen_fitness}")
            if curr_gen_fitness != last_gen_fitness:
                last_gen_fitness = curr_gen_fitness
                same_fitness_cnt = 0
            else:
                same_fitness_cnt += 1

            if same_fitness_cnt == NO_FIT_IMP_STOP_CNT:
                print(f"Early stopped reason: no improvement in fitness for {NO_FIT_IMP_STOP_CNT} generations")
                break

    print(f"Finished after {i} generations")
    print(f"Found {count_unique_pop(P)} different individuals")
    print(f"The population has a fitness of {FITNESS_FX(None, P)}")

    best_ind = min(P, key=lambda ind: C(ind))  # only useful for minimum vertex cover search
    best_found_vc = get_vertex_nodes_idx(best_ind)

    return P, best_ind, best_found_vc, min_vc
