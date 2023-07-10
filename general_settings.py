from eva_algos.fitness_functions import mvc_optimal_fitness
from eva_algos.initial_population import all_ones_pop
from instances.instance_generator import load_instance
from eva_algos.operators import multi_node_swap

NUM_GENERATIONS = 500
GRAPH_INSTANCE = load_instance("instances/5_0_0.0.txt")
NUM_GENES = len(GRAPH_INSTANCE)
MU = 32  # population size
POPULATION_GENERATOR = all_ones_pop
MUTATION_FX = lambda x, y: multi_node_swap(x, y, GRAPH_INSTANCE)
FITNESS_FX = lambda x, y, z: mvc_optimal_fitness(x, y, z, GRAPH_INSTANCE)
ALPHA = 0