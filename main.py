from eva_algos.mu_plus_one_ea_custom import mu_plus_one_ea
from settings import GRAPH_INSTANCE
from instances.instance_renderer import vertex_cover_graph
from misc.mvc_solver import ilp_solve_mvc


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
    # set the random seed
    # # n, delta, mu, alpha
    delta = [2, 4, 8]
    distribution = ["uniform1", "uniform2", "uniform3", "poisson"]
    n = [50, 100, 200, 400]
    mu = [2, 10, 25, 50]

    # alpha = [0.05, 0.1, 0.5] # !!! set POPULATION_GENERATOR to heuristic !!!
    # ea_experiment("./results")

    ea_experiment()
