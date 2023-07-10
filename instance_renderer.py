import networkx as nx
from matplotlib import pyplot as plt


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


def draw_graph(graph, vertex_cover=None):
    """
    Draw a NetworkX graph with optional vertex cover.
    :param graph: The graph to be drawn
    :param vertex_cover: vertex cover of the graph as a list of nodes (optional)
    :return:
    """
    # Use a circular layout for the nodes
    pos = nx.circular_layout(graph)

    # Set node and edge drawing options
    node_options = {"node_size": 500, "alpha": 0.8}
    edge_options = {"width": 2, "alpha": 0.3}

    # Draw non-vertex-cover nodes in a pastel blue color
    non_vertex_cover = [node for node in graph.nodes() if vertex_cover is None or node not in vertex_cover]
    nx.draw_networkx_nodes(graph, pos, nodelist=non_vertex_cover, node_color='lightblue', **node_options)

    if vertex_cover is not None:
        # Draw vertex-cover nodes in a pastel red color
        nx.draw_networkx_nodes(graph, pos, nodelist=vertex_cover, node_color='salmon', **node_options)

    # Draw edges
    nx.draw_networkx_edges(graph, pos, **edge_options)

    # Draw node labels
    nx.draw_networkx_labels(graph, pos)

    plt.show()


def plain_graph(adjacency_matrix):
    """
    basic graph renderer / without vertex cover
    :param adjacency_matrix: adjacency matrix of the graph
    :return:
    """
    graph = create_graph_from_adj_matrix(adjacency_matrix)
    draw_graph(graph)


def vertex_cover_graph(adjacency_matrix, vertex_cover):
    """
    basic graph renderer / with vertex cover
    :param adjacency_matrix: adjacency matrix of the graph
    :param vertex_cover: vertex cover of the graph as a list of nodes
    :return:
    """
    graph = create_graph_from_adj_matrix(adjacency_matrix)
    draw_graph(graph, vertex_cover)


# 3. multiple vertex cover renderer
# another function gets multiple vertex covers and color/size is based on how many times a node is in a vertex cover

# 4. combines 2. and 3.
# where 2 = optimal solution and 3 = solutions from GA => Jakobs fancy graphic


if __name__ == "__main__":
    # Testing the renderer methods
    from instance_generator import load_instance

    adjacency_matrix = load_instance("instances/50_0.2_0.18.txt")
    plain_graph(adjacency_matrix)
    vertex_cover_graph(adjacency_matrix, [0, 1, 2, 3, 4, 5, 6, 7, 8])
