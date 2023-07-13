import itertools
import numpy as np

from eva_algos.utils import get_vertex_nodes_idx, is_vertex_cover
from instances.instance_renderer import vertex_cover_graph
from settings import GRAPH_INSTANCE

EDGE_WEIGHT = 1  # Don't change! Is 1 if there should be an edge weight


def brute_force_diversity_counter(adjacency_matrix, max_vc_len, ignore_isolated_nodes):
    """
    Returns the number of different vertex covers of length max_vc_len or less
    Was used to compare the results of the EA with the maximum possible number of vertex covers
    """
    all_possible_vertex_covers = list(itertools.product([0, 1], repeat=len(adjacency_matrix)))
    all_possible_vertex_covers = [list(vc) for vc in all_possible_vertex_covers if sum(vc) <= max_vc_len]

    filtered_vertex_covers = []
    for vc in all_possible_vertex_covers:
        # Ignore if the node is isolated and the ignore flag is set
        if ignore_isolated_nodes:
            isolated = any(vc[i] == 1 and np.array_equal(adjacency_matrix[i], [0] * len(adjacency_matrix)) for i in
                           range(len(adjacency_matrix)))
            if isolated:
                continue

        # Ignore if the vc is not a valid vertex cover
        if not is_vertex_cover(adjacency_matrix, vc, EDGE_WEIGHT):
            continue

        filtered_vertex_covers.append(vc)

    return filtered_vertex_covers


if __name__ == "__main__":
    EA_FOUND = None
    MAX_VC = 6
    IGNORE_ISOLATED_NODES = True
    BRUTE_FORCE_FOUND = brute_force_diversity_counter(GRAPH_INSTANCE, MAX_VC, IGNORE_ISOLATED_NODES)


    print("Brute force diversity counter")
    print(f"Number of different vertex covers of length {MAX_VC} or less: "
          f"{len(BRUTE_FORCE_FOUND)}")

    if EA_FOUND is not None:
        print("Vertex covers found by the brute force algorithm but not by the EA:")
        for vc in BRUTE_FORCE_FOUND:
            if vc not in EA_FOUND:
                print(vc)
                vertex_cover_graph(GRAPH_INSTANCE, get_vertex_nodes_idx(vc))
