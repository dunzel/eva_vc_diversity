from general_settings import GRAPH_INSTANCE
from instance_renderer import vertex_cover_graph
from mu_plus_one_ea import MU_PLUS_ONE_EA
from mvc_solver import ilp_solve_mvc
from operators import get_vertex_nodes_idx


def ea_experiment():
    MU_PLUS_ONE_EA.run()

    solution, solution_fitness, solution_idx = MU_PLUS_ONE_EA.best_solution()
    print("Parameters of the best solution : {solution}".format(solution=solution))
    print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

    solution_idx = get_vertex_nodes_idx(solution)
    vertex_cover_graph(GRAPH_INSTANCE, solution_idx)


def ilp_experiment():
    mvc = ilp_solve_mvc(GRAPH_INSTANCE)
    vertex_cover_graph(GRAPH_INSTANCE, mvc)


if __name__ == "__main__":
    ilp_experiment()