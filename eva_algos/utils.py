import random

EDGE_WEIGHT = 1  # Don't change! Is 1 if there should be an edge weight


def C(ind, contraint=False, adjacency_matrix=None):
    """Cost function"""
    if not contraint:
        return sum(ind)
    else:
        assert adjacency_matrix is not None
        return sum([ind[i] * adjacency_matrix[i][i] for i in range(len(ind))])


def get_vertex_nodes_idx(ind):
    """
    Gets the indices of the vertex nodes from an individual
    """
    return [i for i, x in enumerate(ind) if x == 1]


def get_ind_from_vertex_nodes_idx(vertex_nodes_idx, n):
    """
    Returns a binary individual from a list of vertex nodes indices
    """
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
            if adjacency_matrix[i][j] == EDGE_WEIGHT and vertex_cover[i] == 0 and vertex_cover[j] == 0:
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


def repair_ind(ind, adjacency_matrix, constraint):
    """
    Repairs an individual that is not a valid solution
    actually it works like the 2-opt heuristic
    """
    V, E = get_graph_representation(adjacency_matrix)

    # shuffle the edges
    random.shuffle(E)

    for e in E:
        if not constraint:
            if ind[e[0]] == 0 and ind[e[1]] == 0:
                new_vc_node = random.choice(e)
        else:
            if adjacency_matrix[e[0]][e[0]] <= adjacency_matrix[e[1]][e[1]]:
                new_vc_node = e[0]
            else:
                new_vc_node = e[1]

        ind[new_vc_node] = 1

    assert is_vertex_cover(adjacency_matrix, ind)

    return ind


def get_unique_pop(P):
    P = set(tuple(x) for x in P)
    P = [list(x) for x in P]
    return P


def count_unique_pop(P):
    return len(get_unique_pop(P))
