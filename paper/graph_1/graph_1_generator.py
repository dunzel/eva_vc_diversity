import os

import numpy as np

from eva_algos.utils import get_ind_from_vertex_nodes_idx
from instances.instance_generator import load_instance
from instances.instance_renderer import vertex_cover_graph
from misc.mvc_solver import ilp_solve_mvc


def get_graph():
    loaded_adjacency_matrix = load_instance("../../instances/50_2.txt")
    vertex_cover_graph(loaded_adjacency_matrix, None, None, "plain_weighted.pdf")

    mvc_optimum = ilp_solve_mvc(loaded_adjacency_matrix)
    vertex_cover_graph(loaded_adjacency_matrix, mvc_optimum, None, "ilp_graph.pdf")

    with open("../../results/unconstrained/n-50_d-2_m-64_uniform1/population.txt", "r") as file:
        population_uncon = np.array([eval(line.strip()) for line in file.readlines()])
    vertex_cover_graph(loaded_adjacency_matrix, None, population_uncon, "uncon_graph_heatmap.pdf")

    with open("../../results/constrained_0.5/n-50_d-2_m-64_uniform1/population.txt", "r") as file:
        population_con_0_5 = np.array([eval(line.strip()) for line in file.readlines()])
    vertex_cover_graph(loaded_adjacency_matrix, None, population_con_0_5, "con_0_5_graph_heatmap.pdf")

    with open("../../results/constrained_0.05/n-50_d-2_m-64_uniform1/population.txt", "r") as file:
        population_con_0_05 = np.array([eval(line.strip()) for line in file.readlines()])
    vertex_cover_graph(loaded_adjacency_matrix, None, population_con_0_05, "con_0_05_graph_heatmap.pdf")


if __name__ == "__main__":
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    get_graph()
