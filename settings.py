import argparse
import re
import time

from eva_algos.fitness_functions import mvc_hamming_diversity
from eva_algos.initial_population import all_ones_pop, heuristic_pop
from instances.instance_generator import load_instance
from eva_algos.operators import multi_node_swap

parser = argparse.ArgumentParser()
parser.add_argument("--n", default=50, type=int, help="Number of vertices.")
parser.add_argument("--delta", default=2, type=int, help="Number of edges per vertex in expectation.")
parser.add_argument("--mu", default=2, type=int, help="Population size.")
parser.add_argument("--distribution", default="uniform1", choices=["uniform1", "uniform2", "uniform3", "poisson"],
                    help="Distribution of mutation probability.")
parser.add_argument("--alpha", default=-1, type=float, help="Approximation factor.")  # -1 means no constraint
args = parser.parse_args([] if "__file__" not in globals() else None)


######################################
# settings for an experiment #
######################################

### main settings ###
GRAPH_FILE_NAME = f"instances/{args.n}_{args.delta}.txt"
MU = args.mu
CONSTRAINT = args.alpha != -1  # if True, the algorithm is constraint and will use (1+alpha) * OPT as an upper bound
ALPHA = args.alpha if CONSTRAINT else 0.0
DISTRIBUTION = args.distribution  # "uniform1", "uniform2", "uniform3" or "poisson"

### fixed settings ###
GRAPH_INSTANCE = load_instance(GRAPH_FILE_NAME)     # Don't change this
NUM_GENES = len(GRAPH_INSTANCE)                     # Don't change this
NUM_GENERATIONS = MU * NUM_GENES**2                 # Don't change this

### early stopping settings ###
EARLY_DIVERSE_STOP = False                                 # stop, if all individuals in the population are different
EARLY_DIVERSE_STOP_CNT = 0                                 # stop, if diversity hasn't increased this many generations
NO_FIT_IMP_STOP_CNT = int(400 * (0.99826**NUM_GENES))      # stop, if fitness has not increased this many generations

### callbacks/function settings ###
POPULATION_GENERATOR = all_ones_pop if not CONSTRAINT else heuristic_pop
MUTATION_FX = multi_node_swap
FITNESS_FX = mvc_hamming_diversity

### message settings ###
DEBUG = False
LOGGING = True

### misc settings ###
RANDOM_SEED = 42
USE_PARALLEL = True
START_TIME = time.time()
TIME_LIMIT = 162000  # 45h time limit

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
    "DISTRIBUTION": DISTRIBUTION,
    "DELTA": DELTA,
    "NUM_GENES": NUM_GENES,
    "MU": MU,
    "NUM_GENERATIONS": NUM_GENERATIONS,
    "EARLY_DIVERSE_STOP": EARLY_DIVERSE_STOP,
    "EARLY_DIVERSE_STOP_CNT": EARLY_DIVERSE_STOP_CNT,
    "NO_FIT_IMP_STOP_CNT": NO_FIT_IMP_STOP_CNT,
    "CONSTRAINT": CONSTRAINT,
    "ALPHA": ALPHA,
    "RANDOM_SEED": RANDOM_SEED,
    "DEBUG": DEBUG,
    "POPULATION_GENERATOR": POPULATION_GENERATOR.__name__,
    "MUTATION_FX": MUTATION_FX.__name__,
    "FITNESS_FX": FITNESS_FX.__name__,
    "USE_PARALLEL": USE_PARALLEL
}

