from eva_algos.fitness_functions import mvc_hamming_diversity
from eva_algos.initial_population import all_ones_pop, all_mvc_pop
from instances.instance_generator import load_instance
from eva_algos.operators import multi_node_swap

#####################
# Change these only #
#####################
GRAPH_INSTANCE = load_instance("instances/5_0.2_0.2.txt")

MU = 32
NUM_GENERATIONS = 5000
EARLY_DIVERSE_STOP = True       # if True, the algorithm will stop if all individuals in the population are different
EARLY_DIVERSE_STOP_CNT = 100    # if True, and the diversity has not increased for this many generations, the algorithm will stop
CONSTRAINED = False             # if True, the algorithm is constrained and will use OPT as an upper bound
ALPHA = 0
RANDOM_SEED = 42

# Callbacks
POPULATION_GENERATOR = all_ones_pop
MUTATION_FX = multi_node_swap
FITNESS_FX = mvc_hamming_diversity

######################
# Don't change these #
######################
NUM_GENES = len(GRAPH_INSTANCE)
