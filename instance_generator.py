import numpy as np


def generate_graph(n, delta):
    """
    :param n: amount of nodes
    :param delta: density of the graph where delta=1 is a complete graph and delta=0 is an isolated graph
    :return:
    """
    adjacency_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                if i < j:
                    if np.random.rand() < delta:
                        adjacency_matrix[i][j] = 1
                        adjacency_matrix[j][i] = 1

    return adjacency_matrix


def save_instance(adjacency_matrix, path):
    """
    :param adjacency_matrix: adjency matrix of the graph
    :param path: path to save the instance
    """
    with open(path, "w") as file:
        file.write(str(len(adjacency_matrix)) + "\n")
        for i in range(len(adjacency_matrix)):
            for j in range(len(adjacency_matrix)):
                if adjacency_matrix[i][j] == 1:
                    file.write(str(i) + " " + str(j) + "\n")


def load_instance(path):
    """
    :param path: path to load the instance
    :return: the adjency matrix of the graph
    """
    with open(path, "r") as file:
        n = int(file.readline())
        adjacency_matrix = np.zeros((n, n))
        for line in file.readlines():
            i, j = line.split()
            adjacency_matrix[int(i)][int(j)] = 1
            adjacency_matrix[int(j)][int(i)] = 1  # undirected graph!

    return adjacency_matrix


def calculate_delta(adjacency_matrix):
    """
    :param adjacency_matrix:
    :return: the density of the graph
    """
    n = len(adjacency_matrix)
    edges = 0
    for i in range(n):
        for j in range(n):
            if i < j:
                if adjacency_matrix[i][j] == 1:
                    edges += 1

    return edges / ((n * (n - 1)) / 2)


def generator_test_samples():
    """
    Generate samples for all combinations of:
    n \in {5, 10, 15}
    delta \in {0, 0.2, 0.5, 0.7, 1}
    """
    for n in [50]:
        for delta in [0.2, 0.5]:
            adjacency_matrix = generate_graph(n, delta)
            resulting_delta = round(calculate_delta(adjacency_matrix), 2)
            save_instance(adjacency_matrix,
                          "instances/" + str(n) + "_" + str(delta) + "_" + str(resulting_delta) + ".txt")


#generator_test_samples()

