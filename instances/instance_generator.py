import numpy as np


def generate_graph(n, delta):
    """
    Generates a random graph with n nodes and a (expected!) density of delta
    :param n: amount of nodes
    :param delta: expected node degree where delta=n-1 is a complete graph and delta=0 is an isolated graph
    :return:
    """
    adjacency_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                if i < j:
                    if np.random.rand() < (delta / n):
                        adjacency_matrix[i][j] = 1
                        adjacency_matrix[j][i] = 1
            else:
                # we save the weight of the node in the diagonal
                # starting from 2 for the weights because 1 is used for indicating normal edges
                adjacency_matrix[i][i] = np.random.randint(2, 2001)

    while calculate_delta(adjacency_matrix) < delta:
        i = np.random.randint(0, n)
        j = np.random.randint(0, n)
        if i != j:
            adjacency_matrix[i][j] = 1
            adjacency_matrix[j][i] = 1

    while calculate_delta(adjacency_matrix) > delta:
        i = np.random.randint(0, n)
        j = np.random.randint(0, n)
        if i != j:
            adjacency_matrix[i][j] = 0
            adjacency_matrix[j][i] = 0

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
                    file.write(str(i) + " " + str(j) + " 0\n")
                # For node weights:
                if i == j:
                    file.write(str(i) + " " + str(j) + " " + str(int(adjacency_matrix[i][i])) + "\n")


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
            i, j, k = line.split()
            if i == j:
                adjacency_matrix[int(i)][int(i)] = int(k)
            else:
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

    # divide by the amount of nodes
    return (2 * edges) / n


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
            filename = "../instances/" + str(n) + "_" + str(delta) + ".txt"
            save_instance(adjacency_matrix, filename)


# will only be executed if this file is run directly
if __name__ == "__main__":
    generator_test_samples([50, 100, 200, 400], [2, 4, 8])
