from fitness_functions import mvc_optimal_fitness
from initial_population import all_ones_pop
from instance_generator import load_instance
from operators import multi_node_swap

NUM_GENERATIONS = 50
GRAPH_INSTANCE = load_instance("instances/5_0.2_0.2.txt")
NUM_GENES = len(GRAPH_INSTANCE)
POPULATION_SIZE = 2
POPULATION_GENERATOR = all_ones_pop
MUTATION_TYPE = lambda x, y: multi_node_swap(x, y, GRAPH_INSTANCE)
FITNESS_FUNCTION = lambda x, y, z: mvc_optimal_fitness(x, y, z, NUM_GENES)

print(GRAPH_INSTANCE)