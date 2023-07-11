from eva_algos.fitness_functions import mvc_hamming_diversity
from eva_algos.initial_population import all_ones_pop
from instances.instance_generator import load_instance
from eva_algos.operators import multi_node_swap

NUM_GENERATIONS = 5000
GRAPH_INSTANCE = load_instance("instances/5_0_0.0.txt")
NUM_GENES = len(GRAPH_INSTANCE)
MU = 32
POPULATION_GENERATOR = all_ones_pop
MUTATION_FX = multi_node_swap
FITNESS_FX = mvc_hamming_diversity
ALPHA = 0
RANDOM_SEED = 42