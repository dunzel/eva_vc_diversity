import random

########################################
# Aux functions for single individuals #
########################################


def C(ind):
    """Cost function"""
    return sum(ind)


def get_vertex_nodes_idx(ind):
    return [i for i, x in enumerate(ind) if x == 1]


def get_ind_from_vertex_nodes_idx(vertex_nodes_idx, n):
    ind = [0] * n
    for i in vertex_nodes_idx:
        ind[i] = 1
    return ind


def is_vertex_cover(adjacency_matrix, vertex_cover):
    """
    Returns True if vertex_cover is a vertex cover of adjacency_matrix
    """
    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix)):
            if adjacency_matrix[i][j] == 1 and vertex_cover[i] == 0 and vertex_cover[j] == 0:
                return False

    return True


def gen_ran_ind(n):
    """
    Generates a random individual of length n
    """
    return [random.randint(0, 1) for _ in range(n)]


def get_graph_representation(adjacency_matrix):
    """
    Returns the graph representation of the adjacency matrix
    :param adjacency_matrix:
    :return: Graph representation (V, E)
    """
    V = list(range(len(adjacency_matrix)))
    E = []

    # Consider that the graph is undirected, so we only need to consider the upper triangle
    for i in range(len(V)):
        for j in range(i + 1, len(V)):
            if adjacency_matrix[i][j]:
                E.append((i, j))

    return V, E


def repair_ind(ind, adjacency_matrix):
    """
    Repairs an individual that is not a valid solution
    """
    V, E = get_graph_representation(adjacency_matrix)

    for e in E:
        if ind[e[0]] == 0 and ind[e[1]] == 0:
            ind[random.choice(e)] = 1

    assert is_vertex_cover(adjacency_matrix, ind)

    return ind




#########################################
# Mutation operators for single parents #
#########################################
# The function header is always the same: def mutation_operator(parent, adjacency_matrix):


def multi_node_swap(parent, adjacency_matrix):
    """
    Selects a node from the vertex cover and removes it.
    To repair the solution, it adds all nodes that are connected to the removed node.
    :param parent: binary list
    :param adjacency_matrix: adjacency matrix of the graph
    :return: mutated offspring that is a valid solution
    WARNING: probably it does not work well with alpha=0 in the constrained case
    """

    # create a copy of the parent that will be mutated
    offspring = parent.copy()

    # get all node indices that are in the vertex cover
    vertex_nodes = get_vertex_nodes_idx(offspring)

    # add a random node to the vertex cover to escape a possible local optimum
    if len(vertex_nodes) == 0:
        random_node = random.randint(0, len(offspring) - 1)
        vertex_nodes.append(random_node)

    selected_node = random.choice(vertex_nodes)

    # get all nodes that are connected to the selected node
    connected_nodes = []
    for i in range(len(adjacency_matrix)):
        if adjacency_matrix[selected_node][i] == 1:
            connected_nodes.append(i)

    # set all connected nodes to 1
    for node in connected_nodes:
        offspring[node] = 1

    # set selected node to 0
    offspring[selected_node] = 0

    return offspring

# if too much time:
# RepairOperation, NodeSwap, EdgeNodeSwap
