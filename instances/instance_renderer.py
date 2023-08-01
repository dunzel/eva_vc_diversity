import networkx as nx
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm

RENDER_SEED = 42
EDGE_WEIGHT = 1  # Don't change! Is 1 if there should be an edge weight


def create_graph_from_adj_matrix(adjacency_matrix):
    """
    Creates a NetworkX graph from the given adjacency matrix.
    :param adjacency_matrix: adjacency matrix of the graph
    :return: graph
    """
    graph = nx.Graph()
    for i in range(len(adjacency_matrix)):
        graph.add_node(i, weight=adjacency_matrix[i][i])
        for j in range(len(adjacency_matrix)):
            if adjacency_matrix[i][j] == EDGE_WEIGHT:
                graph.add_edge(i, j)
    return graph


def draw_graph(graph, vertex_cover=None, population=None, save_path=None):
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
    pos = nx.spring_layout(graph, k=0.6, seed=RENDER_SEED)

    # Set node and edge drawing options
    node_options = {"alpha": 1.0}  # Alpha set to 1.0 for non-transparent nodes
    edge_options = {"width": 2, "alpha": 0.3}

    # Define the normal node size, as well as the minimum and maximum node sizes
    normal_node_size = 500
    min_node_size = 1 * normal_node_size
    max_node_size = 5 * normal_node_size

    # Get the weights of the nodes but sort them by node index
    node_weights = np.array([graph.nodes[i]["weight"] for i in sorted(graph.nodes())])

    # Normalize the weights to range from 0 to 1
    normalized_weights = (node_weights - node_weights.min()) / (node_weights.max() - node_weights.min())

    # Scale the normalized weights to range from min_node_size to max_node_size
    node_sizes = min_node_size + normalized_weights * (max_node_size - min_node_size)

    # Draw non-vertex-cover nodes with a black outline and white fill color, black font
    if population is None:
        non_vertex_cover = [node for node in graph.nodes() if vertex_cover is None or node not in vertex_cover]
        nx.draw_networkx_nodes(graph, pos, nodelist=non_vertex_cover,
                               node_color='white', edgecolors='black',
                               node_size=[node_sizes[i] for i in non_vertex_cover],
                               **node_options)
        nx.draw_networkx_labels(graph, pos, labels={node: node for node in non_vertex_cover}, font_color='black')

        if vertex_cover is not None:
            # Draw vertex-cover nodes with a white outline and black fill color, white font
            nx.draw_networkx_nodes(graph, pos, nodelist=vertex_cover,
                                   node_color='black', edgecolors='white',
                                   node_size=[node_sizes[i] for i in vertex_cover],
                                   **node_options)
            nx.draw_networkx_labels(graph, pos, labels={node: node for node in vertex_cover}, font_color='white')
    else:
        node_list = [node for node in graph.nodes()]
        node_list.sort()

        node_counts = population.sum(axis=0)
        node_colors = node_counts / population.shape[0]
        node_colors = 1 - node_colors

        cmap = cm.get_cmap('Spectral')

        def is_light(rgb):
            """ function to determine if a color is 'light' or 'dark' """
            yiq = ((rgb[0] * 299) + (rgb[1] * 587) + (rgb[2] * 114)) / 1000
            return yiq >= 0.5

        def get_font_color(node_color):
            """ function to get the font color based on the node color """
            rgb = cmap(node_color)[:3]
            if is_light(rgb):
                return 'black'
            else:
                return 'white'

        # font colors for each node
        font_colors = [get_font_color(node_color) for node_color in node_colors]

        # Draw the nodes
        nx.draw_networkx_nodes(graph, pos, nodelist=node_list,
                               node_color=node_colors, edgecolors='black',
                               node_size=node_sizes,
                               cmap='Spectral', vmin=0, vmax=1,
                               **node_options)

        # Draw each label with a separate color
        for node, color in zip(node_list, font_colors):
            nx.draw_networkx_labels(graph, pos, labels={node: node}, font_color=color)

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


def vertex_cover_graph(adjacency_matrix, vertex_cover, population=None, save_path=None):
    """
    basic graph renderer / with vertex cover
    :param adjacency_matrix: adjacency matrix of the graph
    :param vertex_cover: vertex cover of the graph as a list of nodes
    :return:
    """
    graph = create_graph_from_adj_matrix(adjacency_matrix)
    draw_graph(graph, vertex_cover, population, save_path)


if __name__ == "__main__":
    # will only be executed if this file is run directly
    # Testing the renderer methods
    from instance_generator import load_instance
    from misc.mvc_solver import ilp_solve_mvc

    # plain graph
    loaded_adjacency_matrix = load_instance("./50_2.txt")
    plain_graph(loaded_adjacency_matrix)

    # vertex cover graph
    mvc_optimum = ilp_solve_mvc(loaded_adjacency_matrix)
    vertex_cover_graph(loaded_adjacency_matrix, mvc_optimum)

    # heatmap population graph
    with open("../results/constrained_0.05/n-50_d-2_m-64_uniform1/population.txt", "r") as file:
        population = np.array([eval(line.strip()) for line in file.readlines()])
    vertex_cover_graph(loaded_adjacency_matrix, None, population)

