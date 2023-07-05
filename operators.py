import random


def get_vertex_nodes_idx(ind):
    return [i for i, x in enumerate(ind) if x == 1]


def multi_node_swap(offspring, ga_instance, adjency_matrix):
    vertex_nodes = get_vertex_nodes_idx(offspring[0])
    print(vertex_nodes)
    print(offspring[0])
    selected_node = random.choice(vertex_nodes)

    # get all nodes that are connected to the selected node
    connected_nodes = []
    for i in range(len(adjency_matrix)):
        if adjency_matrix[selected_node][i] == 1:
            connected_nodes.append(i)
    print(connected_nodes)
    # set all connected nodes to 1
    for node in connected_nodes:
        offspring[0][node] = 1

    # set selected node to 0
    offspring[0][selected_node] = 0

    print(offspring[0])
    print("-----")
    return offspring

# if too much time:
# RepairOperation, NodeSwap, EdgeNodeSwap