from eva_algos.fitness_functions import mvc_hamming_diversity
from eva_algos.initial_population import all_ones_pop
from instances.instance_generator import load_instance
from eva_algos.operators import multi_node_swap

#####################
# Change these only #
#####################
GRAPH_INSTANCE = load_instance("instances/10_0_0.0.txt")

MU = 1024
NUM_GENERATIONS = 5000
EARLY_DIVERSE_STOP = True   # if True, the algorithm will stop if all individuals in the population are different
CONSTRAINED = True          # if True, the algorithm is constrained and will use OPT as an upper bound
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
