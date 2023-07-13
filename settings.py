import math
import re

from eva_algos.fitness_functions import mvc_hamming_diversity
from eva_algos.initial_population import all_ones_pop, heuristic_pop
from instances.instance_generator import load_instance
from eva_algos.operators import multi_node_swap

######################################
# settings for an experiment #
######################################

### main settings ###
GRAPH_FILE_NAME = "instances/400_4.txt"
MU = 50
CONSTRAINED = False             # if True, the algorithm is constrained and will use (1+alpha) * OPT as an upper bound
ALPHA = 0.05 if CONSTRAINED else 0.0

### fixed settings ###
GRAPH_INSTANCE = load_instance(GRAPH_FILE_NAME)     # Don't change this
NUM_GENES = len(GRAPH_INSTANCE)                     # Don't change this
NUM_GENERATIONS = MU * 2 * NUM_GENES                # Don't change this

### early stopping settings ###
EARLY_DIVERSE_STOP = False                                 # stop, if all individuals in the population are different
EARLY_DIVERSE_STOP_CNT = 0                                 # stop, if diversity hasn't increased this many generations
NO_FIT_IMP_STOP_CNT = int(200 * (0.99826**NUM_GENES))      # stop, if fitness has not increased this many generations

### callbacks/function settings ###
POPULATION_GENERATOR = all_ones_pop if not CONSTRAINED else heuristic_pop
MUTATION_FX = multi_node_swap
FITNESS_FX = mvc_hamming_diversity

### message settings ###
DEBUG = False
LOGGING = True

### misc settings ###
RANDOM_SEED = 42
USE_PARALLEL = True

######################################
# creating dict for logging settings #
######################################

DELTA_match = re.search(r"_([0-9\.]+)\.txt$", GRAPH_FILE_NAME)
if DELTA_match:
    DELTA = int(DELTA_match.group(1))
else:
    DELTA = "None"


SETTINGS_DICT = {
    "GRAPH_FILE_NAME": GRAPH_FILE_NAME,
    "DELTA": DELTA,
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

