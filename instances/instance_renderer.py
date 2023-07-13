import networkx as nx
from matplotlib import pyplot as plt

from settings import RANDOM_SEED


def create_graph_from_adj_matrix(adjacency_matrix):
    """
    Creates a NetworkX graph from the given adjacency matrix.
    :param adjacency_matrix: adjacency matrix of the graph
    :return: graph
    """
    graph = nx.Graph()
    for i in range(len(adjacency_matrix)):
        graph.add_node(i)
        for j in range(len(adjacency_matrix)):
            if adjacency_matrix[i][j] == 1:
                graph.add_edge(i, j)
    return graph


def draw_graph(graph, vertex_cover=None, save_path=None):
    """
    Draw a NetworkX graph with optional vertex cover.
    :param graph: The graph to be drawn
    :param vertex_cover: vertex cover of the graph as a list of nodes (optional)
    :param scale_factor: The factor by which to scale the positions of the nodes
    :return:
    """
    # square figure
    plt.figure(figsize=(15, 15))

    # Use a circular layout for the nodes
    pos = nx.spring_layout(graph, k=0.70, seed=RANDOM_SEED)

    # Set node and edge drawing options
    node_options = {"node_size": 500, "alpha": 1.0}  # Alpha set to 1.0 for non-transparent nodes
    edge_options = {"width": 2, "alpha": 0.3}

    # Draw non-vertex-cover nodes with a black outline and white fill color, black font
    non_vertex_cover = [node for node in graph.nodes() if vertex_cover is None or node not in vertex_cover]
    nx.draw_networkx_nodes(graph, pos, nodelist=non_vertex_cover, edgecolors='black', node_color='white', **node_options)
    nx.draw_networkx_labels(graph, pos, labels={node: node for node in non_vertex_cover}, font_color='black')

    if vertex_cover is not None:
        # Draw vertex-cover nodes with a white outline and black fill color, white font
        nx.draw_networkx_nodes(graph, pos, nodelist=vertex_cover, edgecolors='white', node_color='black', **node_options)
        nx.draw_networkx_labels(graph, pos, labels={node: node for node in vertex_cover}, font_color='white')

    # Draw edges
    nx.draw_networkx_edges(graph, pos, **edge_options)

    if save_path is not None:
        plt.savefig(save_path)
    else:
        plt.show()


def plain_graph(adjacency_matrix):
    """
    basic graph renderer / without vertex cover
    :param adjacency_matrix: adjacency matrix of the graph
    :return:
    """
    graph = create_graph_from_adj_matrix(adjacency_matrix)
    draw_graph(graph)


def vertex_cover_graph(adjacency_matrix, vertex_cover, save_path=None):
    """
    basic graph renderer / with vertex cover
    :param adjacency_matrix: adjacency matrix of the graph
    :param vertex_cover: vertex cover of the graph as a list of nodes
    :return:
    """
    graph = create_graph_from_adj_matrix(adjacency_matrix)
    draw_graph(graph, vertex_cover, save_path)


# 3. multiple vertex cover renderer
# another function gets multiple vertex covers and color/size is based on how many times a node is in a vertex cover

# 4. combines 2. and 3.
# where 2 = optimal solution and 3 = solutions from GA => Jakobs fancy graphic


if __name__ == "__main__":
    # will only be executed if this file is run directly
    # Testing the renderer methods
    from instance_generator import load_instance
    from misc.mvc_solver import ilp_solve_mvc

    loaded_adjacency_matrix = load_instance("5_0.2_0.2.txt")
    plain_graph(loaded_adjacency_matrix)
    mvc_optimum = ilp_solve_mvc(loaded_adjacency_matrix)
    vertex_cover_graph(loaded_adjacency_matrix, mvc_optimum)
