import networkx as nx
from matplotlib import pyplot as plt

from general_ea_settings import GRAPH_INSTANCE
from instance_generator import load_instance


def plain_graph(adjacency_matrix):
    """
    basic graph renderer / without vertex cover
    :param adjacency_matrix: adjency matrix of the graph
    :return:
    """
    graph = nx.Graph()
    for i in range(len(adjacency_matrix)):
        graph.add_node(i)
        for j in range(len(adjacency_matrix)):
            if adjacency_matrix[i][j] == 1:
                graph.add_edge(i, j)
                
    start_pos = nx.spring_layout(graph, seed=100)
    nx.draw(graph, with_labels=True, pos=start_pos)
    plt.show()


# 2. vertex cover renderer
# should also render Vertex Cover somehow
# colors nodes that are in the vertex cover
def vertex_cover_graph(adjacency_matrix, vertex_cover):
    """
    basic graph renderer / without vertex cover
    :param adjacency_matrix: adjency matrix of the graph
    :param vertex_cover: vertex cover of the graph as a list of nodes
    :return:
    """
    graph = nx.Graph()
    for i in range(len(adjacency_matrix)):
        graph.add_node(i)
        for j in range(len(adjacency_matrix)):
            if adjacency_matrix[i][j] == 1:
                graph.add_edge(i, j)

    start_pos = nx.spring_layout(graph, seed=100)
    nx.draw(graph, with_labels=True, pos=start_pos)
    nx.draw_networkx_nodes(graph, start_pos, nodelist=vertex_cover, node_color='r', node_size=500)
    plt.show()

# adjacency_matrix = load_instance("instances/5_0.2_0.2.txt")
# vertex_cover_graph(adjacency_matrix, [4, 7, 10])


# 3. multiple vertex cover renderer
# another function gets multiple vertex covers and color/size is based on how many times a node is in a vertex cover

# 4. combines 2. and 3.
# where 2 = optimal solution and 3 = solutions from GA => Jakobs fancy graphic