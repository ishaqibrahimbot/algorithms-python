"""
We are going to implement the random contraction algorithm for graphs. Let's do some brainstorming for it.

Input: an adjacency list representing a graph.
Output: The minimum cut for the graph, i.e. two sets A and B, each containing a unique group of nodes

Basic idea: with no. of nodes = n, run n-2 iterations and on every iteration, pick an edge at random.
            Then, take the nodes corresponding to that edge and merge them into a supernode. Delete
            any self-loops, if any. Continue this process until you are left with two supernodes,
            which should be the case if you run n-2 iterations. Output the number of edges between these
            two supernodes. Once we have this basic algorithm, we just need to run it a large number
            of times to get the actual min-cut.
"""
import random
import copy

def load_graph():
    graph = {}
    with open("kargerMinCut.txt", 'r') as f:
        for line in f.readlines():
            row = line.split("\t")[:-1]
            graph[row[0]] = row[1:]
    return graph

def get_edge_list(graph):
    edge_list = []
    new_graph = copy.deepcopy(graph)
    for i, node in enumerate(new_graph.keys()):
        adjacent_node_list = new_graph[node]
        while len(adjacent_node_list) > 0:
            current_adjacent_node = adjacent_node_list[0]
            new_edge = (node, current_adjacent_node)
            # print(new_edge)
            edge_list.append(new_edge)
            new_graph[node].pop(0)
            new_graph[current_adjacent_node].pop(new_graph[current_adjacent_node].index(node))

    return edge_list

def filter_node_list(node_list, reference_node, new_node):
    for i, node in enumerate(node_list):
        if node == reference_node:
            node_list[i] = new_node
    
    return node_list


def min_cut(orig_graph):
    graph = copy.deepcopy(orig_graph)
    n = len(graph) #length of graph

    while(len(graph.keys()) > 2):
        edge_list = get_edge_list(graph)
        u, v = random.choice(edge_list)
        graph[u] = [node for node in graph[u] if node != v]
        graph[v] = [node for node in graph[v] if node != u]
        new_node = u + "_" + v
        for adjacent_node in graph[u]:
            graph[adjacent_node] = filter_node_list(graph[adjacent_node], u, new_node)

        for adjacent_node in graph[v]:
            graph[adjacent_node] = filter_node_list(graph[adjacent_node], v, new_node)

        graph[new_node] = graph[u] + graph[v]
        del graph[u]
        del graph[v]

    num_keys_remaining = len(graph.keys())
    num_edges = len(list(graph.values())[0])

    return num_edges


orig_graph = load_graph()
trials = []

for i in range(100):
    print(i)
    trials.append(min_cut(orig_graph))

print(min(trials))