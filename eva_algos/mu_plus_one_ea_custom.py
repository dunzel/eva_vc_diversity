import os
import random
from datetime import datetime
from multiprocessing import Pool

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from eva_algos.utils import C, get_vertex_nodes_idx, get_ind_from_vertex_nodes_idx, count_unique_pop
from instances.instance_renderer import vertex_cover_graph
from settings import NUM_GENERATIONS, MU, ALPHA, GRAPH_INSTANCE, POPULATION_GENERATOR, \
    FITNESS_FX, MUTATION_FX, NUM_GENES, EARLY_DIVERSE_STOP, CONSTRAINT, EARLY_DIVERSE_STOP_CNT, \
    NO_FIT_IMP_STOP_CNT, RANDOM_SEED, DELTA, SETTINGS_DICT, LOGGING, USE_PARALLEL
from misc.mvc_solver import ilp_solve_mvc


def ind_fit_fx(ind, P, FITNESS_FX):
    """
    Fitness function for the individuals in the population
    """
    return FITNESS_FX(ind, P)


def mu_plus_one_ea():
    """
    Diversity maximising (𝜇 + 1)-EA
    :return: the diverse population, the so far best individual, the so far best vertex cover, the minimum vertex cover
    """
    random.seed(RANDOM_SEED)

    #################
    # Logging Setup #
    #################

    # Create logging directory
    log_dir = "./results/"
    if CONSTRAINT:
        log_dir += "constrained" + "_" + str(ALPHA) + "/"
    else:
        log_dir += "unconstrained/"
    log_dir += "n-" + str(NUM_GENES) + "_d-" + str(DELTA) + "_m-" + str(MU) + "/"

    if LOGGING:
        # create the log directory if it does not exist
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # save SETTING_DICT into settings.txt
        with open(log_dir + "settings.txt", "w") as f:
            for key, value in SETTINGS_DICT.items():
                f.write(f"{key}: {value}\n")

        # delete log txt files if they exist
        if os.path.exists(log_dir + "log.txt"):
            os.remove(log_dir + "log.txt")

        # write start time to start_time.txt
        with open(log_dir + "start_time.txt", "w") as f:
            start_time = datetime.now()
            f.write(str(start_time))

    ####################################
    # Start of the mu+1 implementation #
    ####################################

    # Calculate the minimum vertex cover
    min_vc = ilp_solve_mvc(GRAPH_INSTANCE)
    min_vc_ind = get_ind_from_vertex_nodes_idx(min_vc, NUM_GENES)
    OPT = C(min_vc_ind, True, GRAPH_INSTANCE) if CONSTRAINT else np.Inf

    if LOGGING:
        # save min_vc_ind to file
        with open(log_dir + "ilp_min_vc.txt", "w") as f:
            f.write(str(min_vc))

        # save min_vc_ind as plot to file
        vertex_cover_graph(GRAPH_INSTANCE, min_vc, log_dir + "ilp_min_vc.png")

        print(f"Max mu+1 generations: {NUM_GENERATIONS}")
        print("generation, unique_ind, population_fitness, best_ind_vc_cnt")

    # Initialise population with 𝜇 individuals of a same random or heuristic individual
    P = POPULATION_GENERATOR(MU, NUM_GENES, ALPHA, OPT, GRAPH_INSTANCE, min_vc_ind)

    # Early stopping variables and iteration counter
    last_gen_diversity = same_diversity_cnt = last_gen_fitness = same_fitness_cnt = i = 0

    # Initialise Pool object outside the loop
    if USE_PARALLEL:
        pool = Pool()

    for i in range(NUM_GENERATIONS):
        # Choose a random individual from the population and mutate it
        T = random.choice(P)
        T_m = MUTATION_FX(T, GRAPH_INSTANCE)

        # Check if the cost of the mutated individual is in the range of the relaxed optimal solution
        if C(T_m, CONSTRAINT, GRAPH_INSTANCE) <= (1 + ALPHA) * OPT:
            P.append(T_m)

        # Remove the individual with the lowest fitness from the population
        # i.e. the ind with the lowest contribution to diversity
        if len(P) == MU + 1:
            if USE_PARALLEL:
                fitnesses = pool.starmap(ind_fit_fx, [(ind, P, FITNESS_FX) for ind in P])
                worst_ind = P[fitnesses.index(max(fitnesses))]
            else:
                worst_ind = max(P, key=lambda ind: FITNESS_FX(ind, P))

            P.remove(worst_ind)

        assert len(P) == MU

        ########################################################################
        # Logging: generation, unique_ind, population_fitness, best_ind_vc_cnt #
        ########################################################################
        # Check diversity
        generation = i
        unique_ind = count_unique_pop(P)
        population_fitness = FITNESS_FX(None, P)
        best_ind_vc_cnt = min(P, key=lambda ind: C(ind, CONSTRAINT, GRAPH_INSTANCE))

        if LOGGING:
            log_line = f"{generation},{unique_ind},{population_fitness}," \
                       f"{C(best_ind_vc_cnt, CONSTRAINT, GRAPH_INSTANCE)}\n"
            print(log_line, end="")
            # save generation, unique_ind, population_fitness, best_ind_fit to file
            with open(log_dir + "log.txt", "a") as f:
                f.write(log_line)

        #################################################################
        # The following sections are not part of the original algorithm #
        #################################################################
        # Early stopping if maximum diversity is reached
        if EARLY_DIVERSE_STOP:
            # stops if all individuals in the population are different
            # counts the number of unique individuals in the population
            if unique_ind == len(P):
                print(f"Early stopped reason: max diversity reached")
                break

        # Early stopping if no improvement in diversity for EARLY_DIVERSE_STOP_CNT generations
        if EARLY_DIVERSE_STOP_CNT > 0:
            if unique_ind > last_gen_diversity:
                last_gen_diversity = unique_ind
                same_diversity_cnt = 0
            else:
                same_diversity_cnt += 1

            if same_diversity_cnt == EARLY_DIVERSE_STOP_CNT:
                print(f"Early stopped reason: no improvement in diversity for {EARLY_DIVERSE_STOP_CNT} generations")
                break

        # Early stopping if no improvement in fitness for NO_FIT_IMP_STOP_CNT generations
        if NO_FIT_IMP_STOP_CNT > 0:
            curr_gen_fitness = FITNESS_FX(None, P)
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
    print(f"The best individual has a vertex cover of {C(min(P, key=lambda ind: C(ind)), CONSTRAINT, GRAPH_INSTANCE)} nodes")
    print(f"The ilp solution has a vertex cover of {C(min_vc_ind, CONSTRAINT, GRAPH_INSTANCE)} nodes")

    if USE_PARALLEL:
        pool.close()
        pool.join()

    ######################
    # Last logging steps #
    ######################
    best_ind = min(P, key=lambda ind: C(ind, CONSTRAINT, GRAPH_INSTANCE))  # only useful for minimum vertex cover search
    best_found_vc = get_vertex_nodes_idx(best_ind)

    if LOGGING:
        # saving the best individual to file
        with open(log_dir + "best_found_vc.txt", "w") as f:
            f.write(str(best_found_vc))

        # saving the best individual as plot to file
        vertex_cover_graph(GRAPH_INSTANCE, best_found_vc, log_dir + "best_found_vc.png")

        # saving the population to file
        with open(log_dir + "population.txt", "w") as f:
            for ind in P:
                f.write(str(ind) + "\n")

        # saving every individual of the population as plot to the directory pop_plots
        pop_plots_dir = log_dir + "pop_plots/"
        if not os.path.exists(pop_plots_dir):
            os.makedirs(pop_plots_dir)
        for i, ind in enumerate(P):
            vertex_cover_graph(GRAPH_INSTANCE, get_vertex_nodes_idx(ind), pop_plots_dir + f"ind_{i}.png")

        # plotting the log
        df = pd.read_csv(log_dir + "log.txt", header=None, names=["generation", "unique_ind", "population_fitness", "best_ind_vc_cnt"])
        df.plot(x="generation", y=["unique_ind", "population_fitness", "best_ind_vc_cnt"], subplots=True, layout=(3, 1), figsize=(10, 10))

        plt.savefig(log_dir + "log.png")

        # write end time to file
        with open(log_dir + "end_time.txt", "w") as f:
            f.write(str(datetime.now()))

        # write computation time to file
        with open(log_dir + "computation_time.txt", "w") as f:
            f.write(str(datetime.now() - start_time))


    return P, best_ind, best_found_vc, min_vc
