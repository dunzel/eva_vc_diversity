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
GRAPH_FILE_NAME = "instances/unconstrained/400_2.txt"
MU = 50
ALPHA = 0.05
CONSTRAINED = False             # if True, the algorithm is constrained and will use (1+alpha) * OPT as an upper bound

### fixed settings ###
GRAPH_INSTANCE = load_instance(GRAPH_FILE_NAME)     # Don't change this
NUM_GENES = len(GRAPH_INSTANCE)                     # Don't change this
NUM_GENERATIONS = MU * 2 * NUM_GENES                # Don't change this

### early stopping settings ###
EARLY_DIVERSE_STOP = False                          # stop, if all individuals in the population are different
EARLY_DIVERSE_STOP_CNT = 0                          # stop, if diversity hasn't increased for this many generations
NO_FIT_IMP_STOP_CNT = math.sqrt(NUM_GENERATIONS)    # stop, if fitness has not increased for this many generations

### callbacks/function settings ###
POPULATION_GENERATOR = all_ones_pop if not CONSTRAINED else heuristic_pop
MUTATION_FX = multi_node_swap
FITNESS_FX = mvc_hamming_diversity

### message settings ###
DEBUG = False
LOGGING = False

### misc settings ###
RANDOM_SEED = 42

######################################
# creating dict for logging settings #
######################################

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

