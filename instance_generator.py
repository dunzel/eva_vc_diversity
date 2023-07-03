import numpy as np


def generate_graph(n, delta):
    """
    :param n: amount of nodes
    :param delta: density of the graph where delta=1 is a complete graph and delta=0 is an isolated graph
    :return:
    """
    adjency_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                if np.random.rand() < delta:
                    adjency_matrix[i][j] = 1

    return adjency_matrix


def save_instance(adjency_matrix, path):
    """
    :param adjency_matrix: adjency matrix of the graph
    :param path: path to save the instance
    """
    with open(path, "w") as file:
        file.write(str(len(adjency_matrix)) + "\n")
        for i in range(len(adjency_matrix)):
            for j in range(len(adjency_matrix)):
                if adjency_matrix[i][j] == 1:
                    file.write(str(i) + " " + str(j) + "\n")


def load_instance(path):
    """
    :param path: path to load the instance
    :return: the adjency matrix of the graph
    """
    with open(path, "r") as file:
        n = int(file.readline())
        adjency_matrix = np.zeros((n, n))
        for line in file.readlines():
            i, j = line.split()
            adjency_matrix[int(i)][int(j)] = 1

    return adjency_matrix


def calculate_delta(adjency_matrix):
    """
    :param adjency_matrix:
    :return: the density of the graph
    """
    n = len(adjency_matrix)
    edges = 0
    for i in range(n):
        for j in range(n):
            if adjency_matrix[i][j] == 1:
                edges += 1

    return edges / (n * (n - 1))


def generator_test_samples():
    """
    Generate samples for all combinations of:
    n \in {5, 10, 15}
    delta \in {0, 0.2, 0.5, 0.7, 1}
    """
    for n in [5, 10, 15]:
        for delta in [0, 0.2, 0.5, 0.7, 1]:
            adjency_matrix = generate_graph(n, delta)
            resulting_delta = round(calculate_delta(adjency_matrix), 2)
            save_instance(adjency_matrix, "instances/" + str(n) + "_" + str(delta) + "_" + str(resulting_delta) + ".txt")
