from gurobipy import *


def ilp_solve_mvc(adjacency_matrix):
    # convert adjacency matrix to graph
    V = list(range(len(adjacency_matrix)))
    E = []

    # consider that the graph is undirected, so we only need to consider the upper triangle
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

    # objective function
    model.setObjective(quicksum(x[v] for v in V), GRB.MINIMIZE)

    # constraints
    for e in E:
        model.addConstr(x[e[0]] + x[e[1]] >= 1)

    # solve the model
    model.optimize()

    return [v for v in V if x[v].x == 1]