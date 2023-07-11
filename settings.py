from eva_algos.fitness_functions import mvc_hamming_diversity, mvc_hamming_diversity_cmp
from eva_algos.initial_population import all_ones_pop, all_mvc_pop, heuristic_pop
from instances.instance_generator import load_instance
from eva_algos.operators import multi_node_swap

#####################
# Change these only #
#####################
GRAPH_INSTANCE = load_instance("instances/5_0.2_0.2.txt")

MU = 50
NUM_GENERATIONS = 10000
EARLY_DIVERSE_STOP = True       # if True, the algorithm will stop if all individuals in the population are different
EARLY_DIVERSE_STOP_CNT = 1000      # if True, and the diversity has not increased for this many generations, the algorithm will stop
CONSTRAINED = True              # if True, the algorithm is constrained and will use OPT as an upper bound
ALPHA = 1
RANDOM_SEED = 42
DEBUG = True

# Callbacks
POPULATION_GENERATOR = heuristic_pop
MUTATION_FX = multi_node_swap
FITNESS_FX = mvc_hamming_diversity

######################
# Don't change these #
######################
NUM_GENES = len(GRAPH_INSTANCE)
