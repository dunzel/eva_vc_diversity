from gurobipy import *


def ilp_solve_mvc(adjacency_matrix):
    """
    Solves the minimum vertex cover problem using an ILP formulation
    :param adjacency_matrix: the adjacency matrix of the graph
    :return: the minimum vertex cover
    """

    # Convert adjacency matrix to graph
    V = list(range(len(adjacency_matrix)))
    E = []

    # Consider that the graph is undirected, so we only need to consider the upper triangle
    for i in range(len(V)):
        for j in range(i + 1, len(V)):
            if adjacency_matrix[i][j]:
                E.append((i, j))

    model = Model("MVC")
    model.modelSense = GRB.MINIMIZE

    # Defining the variables
    x = {}
    for v in V:
        x[v] = model.addVar(name="x_" + str(v), vtype=GRB.BINARY)

    model.update()

    # Objective function
    model.setObjective(quicksum(x[v] for v in V), GRB.MINIMIZE)

    # Constraints
    for e in E:
        model.addConstr(x[e[0]] + x[e[1]] >= 1)

    # Solve the model
    model.optimize()

    # Return the solution as a list of vertex indices
    return [v for v in V if x[v].x == 1]
