import numpy as np


def generate_graph(n, delta):
    """
    Generates a random graph with n nodes and a (expected!) density of delta
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
    Saves an instance to a file
    :param adjacency_matrix: adjacency matrix of the graph
    :param path: path to save the instance
    """
    with open(path, "w") as file:
        # first line is the amount of nodes
        file.write(str(len(adjacency_matrix)) + "\n")

        # write the edges to the file
        for i in range(len(adjacency_matrix)):
            for j in range(len(adjacency_matrix)):
                if adjacency_matrix[i][j] == 1:
                    file.write(str(i) + " " + str(j) + "\n")


def load_instance(path):
    """
    Loads an instance from a file
    :param path: path to load the instance
    :return: the adjacency matrix of the graph
    """
    with open(path, "r") as file:
        # first line is the amount of nodes
        n = int(file.readline())

        # initialize the adjacency matrix
        adjacency_matrix = np.zeros((n, n))

        # read the edges from the file
        for line in file.readlines():
            i, j = line.split()
            adjacency_matrix[int(i)][int(j)] = 1
            adjacency_matrix[int(j)][int(i)] = 1  # undirected graph!

    return adjacency_matrix


def calculate_delta(adjacency_matrix):
    """
    Calculates the density of the graph
    :param adjacency_matrix: adjacency matrix of the graph
    :return: the "real" density of the graph. May differ from the density that was used to generate the graph
    """
    n = len(adjacency_matrix)
    edges = 0
    for i in range(n):
        for j in range(n):
            if i < j:
                if adjacency_matrix[i][j] == 1:
                    edges += 1

    # divide by the amount of possible edges in an undirected graph without self-loops
    return edges / ((n * (n - 1)) / 2)


def generator_test_samples(ns, deltas):
    """
    Generates test samples for the given mu and densities
    :param ns: is a list of the amount of nodes for a graph
    :param deltas: is a list of densities that should be generated for each given n
    :return: saves the instances in the instances folder
    """
    for n in ns:
        for delta in deltas:
            adjacency_matrix = generate_graph(n, delta)
            resulting_delta = round(calculate_delta(adjacency_matrix), 2)
            filename = "./instances" + str(n) + "_" + str(delta) + "_" + str(resulting_delta) + ".txt"
            save_instance(adjacency_matrix, filename)


# will only be executed if this file is run directly
if __name__ == "__main__":
    generator_test_samples([100], [0.02, 0.05])

