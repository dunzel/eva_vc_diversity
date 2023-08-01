from gurobipy import *

from eva_algos.utils import get_graph_representation


def ilp_solve_mvc(adjacency_matrix, constrained=True):
    """
    Solves the minimum vertex cover problem using an ILP formulation
    :param adjacency_matrix: the adjacency matrix of the graph
    :param constrained: whether to use the constrained formulation or not
    :return: the minimum vertex cover
    """

    # Convert adjacency matrix to graph
    V, E = get_graph_representation(adjacency_matrix)

    model = Model("MVC")
    model.setParam('TimeLimit', 5 * 60)  # 5 minute time limit
    model.modelSense = GRB.MINIMIZE

    # Defining the variables
    x = {}
    for v in V:
        x[v] = model.addVar(name="x_" + str(v), vtype=GRB.BINARY)

    model.update()

    # Objective function
    if not constrained:
        model.setObjective(quicksum(x[v] for v in V), GRB.MINIMIZE)
    else:
        model.setObjective(quicksum(x[v] * adjacency_matrix[v][v] for v in V), GRB.MINIMIZE)

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
