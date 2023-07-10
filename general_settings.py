from eva_algos.fitness_functions import mvc_optimal_fitness
from eva_algos.initial_population import all_ones_pop
from instances.instance_generator import load_instance
from eva_algos.operators import multi_node_swap

NUM_GENERATIONS = 500
GRAPH_INSTANCE = load_instance("instances/50_0.2_0.18.txt")
NUM_GENES = len(GRAPH_INSTANCE)
POPULATION_SIZE = 32
POPULATION_GENERATOR = all_ones_pop
MUTATION_TYPE = lambda x, y: multi_node_swap(x, y, GRAPH_INSTANCE)
FITNESS_FUNCTION = mvc_optimal_fitness
