from gurobipy import *

from eva_algos.utils import get_graph_representation


def ilp_solve_mvc(adjacency_matrix):
    """
    Solves the minimum vertex cover problem using an ILP formulation
    :param adjacency_matrix: the adjacency matrix of the graph
    :return: the minimum vertex cover
    """

    # Convert adjacency matrix to graph
    V, E = get_graph_representation(adjacency_matrix)

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
    vertex_cover_idx = [v for v in V if x[v].x == 1]
    print("Vertex cover found by the ILP solver:")
    print(vertex_cover_idx)
    print("Number of vertices in the ILP vertex cover:")
    print(len(vertex_cover_idx))

    return vertex_cover_idx
