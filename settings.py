import re

from eva_algos.fitness_functions import mvc_hamming_diversity, mvc_hamming_diversity_cmp
from eva_algos.initial_population import all_ones_pop, all_mvc_pop, heuristic_pop
from instances.instance_generator import load_instance
from eva_algos.operators import multi_node_swap

GRAPH_FILE_NAME = "instances/100_8.txt"
GRAPH_INSTANCE = load_instance(GRAPH_FILE_NAME)
NUM_GENES = len(GRAPH_INSTANCE)  # Don't change this

MU = 2
NUM_GENERATIONS = MU * 2 * NUM_GENES
EARLY_DIVERSE_STOP = False      # if True, the algorithm will stop if all individuals in the population are different
EARLY_DIVERSE_STOP_CNT = 0      # if True, and the diversity has not increased for this many generations, the algorithm will stop
NO_FIT_IMP_STOP_CNT = 100       # if True, and the fitness has not increased for this many generations, the algorithm will stop
CONSTRAINED = False             # if True, the algorithm is constrained and will use OPT as an upper bound
ALPHA = 0.05
RANDOM_SEED = 42
DEBUG = False
LOGGING = False

# Callbacks
POPULATION_GENERATOR = all_ones_pop
MUTATION_FX = multi_node_swap
FITNESS_FX = mvc_hamming_diversity

#######################################
# creating dict for preserve settings #
#######################################

EXPECTED_DELTA_match = re.search(r"_([0-9\.]+)_", GRAPH_FILE_NAME)
if EXPECTED_DELTA_match:
    EXPECTED_DELTA = float(EXPECTED_DELTA_match.group(1))
else:
    EXPECTED_DELTA = None

RESULTED_DELTA_match = re.search(r"_([0-9\.]+)\.txt$", GRAPH_FILE_NAME)
if RESULTED_DELTA_match:
    RESULTED_DELTA = float(RESULTED_DELTA_match.group(1))
else:
    RESULTED_DELTA = None


SETTINGS_DICT = {
    "GRAPH_FILE_NAME": GRAPH_FILE_NAME,
    "EXPECTED_DELTA": EXPECTED_DELTA,
    "RESULTED_DELTA": RESULTED_DELTA,
    "NUM_GENES": NUM_GENES,
    "MU": MU,
    "NUM_GENERATIONS": NUM_GENERATIONS,
    "EARLY_DIVERSE_STOP": EARLY_DIVERSE_STOP,
    "EARLY_DIVERSE_STOP_CNT": EARLY_DIVERSE_STOP_CNT,
    "NO_FIT_IMP_STOP_CNT": NO_FIT_IMP_STOP_CNT,
    "CONSTRAINED": CONSTRAINED,
    "ALPHA": ALPHA,
    "RANDOM_SEED": RANDOM_SEED,
    "DEBUG": DEBUG,
    "POPULATION_GENERATOR": POPULATION_GENERATOR.__name__,
    "MUTATION_FX": MUTATION_FX.__name__,
    "FITNESS_FX": FITNESS_FX.__name__,
}

