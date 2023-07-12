import random

from eva_algos.mu_plus_one_ea_custom import mu_plus_one_ea
from settings import GRAPH_INSTANCE, RANDOM_SEED
from instances.instance_renderer import vertex_cover_graph
from mvc_solver import ilp_solve_mvc


def ea_experiment():
    P, best_ind, best_found_vc, min_vc = mu_plus_one_ea()
    print("Diverse population: ", end="")
    print(P)
    print("Best individual: ", end="")
    print(best_ind)
    vertex_cover_graph(GRAPH_INSTANCE, best_found_vc)
    vertex_cover_graph(GRAPH_INSTANCE, min_vc)



def ilp_experiment():
    mvc = ilp_solve_mvc(GRAPH_INSTANCE)
    vertex_cover_graph(GRAPH_INSTANCE, mvc)


if __name__ == "__main__":
    # # set the random seed
    # # # n, delta, mu, alpha
    # n = [50, 100, 200, 400]
    # delta = [2, 4, 8]
    # mu = []
    # alpha = []
    # # ea_experiment("./results")

    ea_experiment()
