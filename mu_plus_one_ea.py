from general_ea_settings import \
    NUM_GENERATIONS, POPULATION_GENERATOR, POPULATION_SIZE, NUM_GENES, MUTATION_TYPE, FITNESS_FUNCTION
from pygad import pygad

################################################
# Setting for the mu+1 EA - no need to change  #
################################################
NUM_PARENTS_MATING = 1
INITIAL_POPULATION = POPULATION_GENERATOR(POPULATION_SIZE, NUM_GENES)

# assuming an individual is an array of 0s and 1s
GENE_TYPE = int
INIT_RANGE_LOW = 0
INIT_RANGE_HIGH = 1

PARENTAL_SELECTION_TYP = 'random'
KEEP_PARENTS = -1  # we keep all parents as its only one
KEEP_ELITISM = 0
CROSSOVER_TYPE = None

MUTATION_NUM_GENES = 1  # hacky: we only mutate the whole individual at once
RANDOM_SEED = 42
################################################

MU_PLUS_ONE_EA = pygad.GA(num_generations=NUM_GENERATIONS,
                          num_parents_mating=NUM_PARENTS_MATING,
                          initial_population=INITIAL_POPULATION,
                          gene_type=GENE_TYPE,
                          init_range_low=INIT_RANGE_LOW,
                          init_range_high=INIT_RANGE_HIGH,
                          parent_selection_type=PARENTAL_SELECTION_TYP,
                          keep_parents=KEEP_PARENTS,
                          keep_elitism=KEEP_ELITISM,
                          crossover_type=CROSSOVER_TYPE,
                          mutation_type=MUTATION_TYPE,
                          mutation_num_genes=MUTATION_NUM_GENES,
                          random_seed=RANDOM_SEED,
                          fitness_func=FITNESS_FUNCTION,
                          )
