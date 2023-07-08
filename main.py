import numpy as np

from general_ea_settings import GRAPH_INSTANCE
from instance_renderer import vertex_cover_graph
from mu_plus_one_ea import MU_PLUS_ONE_EA
from operators import get_vertex_nodes_idx

if __name__ == "__main__":
    MU_PLUS_ONE_EA.run()


    solution, solution_fitness, solution_idx = MU_PLUS_ONE_EA.best_solution()
    print("Parameters of the best solution : {solution}".format(solution=solution))
    print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

    MU_PLUS_ONE_EA.plot_fitness()
    #for individual in MU_PLUS_ONE_EA.population:
    #    solution_idx = get_vertex_nodes_idx(individual)
    #    vertex_cover_graph(GRAPH_INSTANCE, solution_idx)
    solution_idx = get_vertex_nodes_idx(solution)
    vertex_cover_graph(GRAPH_INSTANCE, solution_idx)


