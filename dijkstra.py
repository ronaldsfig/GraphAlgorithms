from weightedGraph import WeightedGraph
from minHeap import MinHeap
import numpy as numpy


def dijkstra(matrix, root):
    cost = [[-1, 0] for i in range(len(matrix))]
    cost[root] = [0, root]
    heap = MinHeap()
    heap.insert(0, root)
    while heap.size() > 0:
        total_weight, node = heap.extractMin()
        for i in range(len(matrix)):
            if matrix[node][i] != 0:
                weight_sum = total_weight + matrix[node][i]
                if cost[i][0] == -1 or cost[i][0] > weight_sum:
                    cost[i] = [weight_sum, node]
                    heap.insert(weight_sum, i)
    return cost


def dijkstraGraph(graph, root):
    result = WeightedGraph()
    cost = [[-1, 0] for i in range(graph.num_nodes)]
    cost[root] = [0, root]
    heap = MinHeap()
    heap.insert(0, root)

    while heap.size() > 0:
        total_weight, node_from = heap.extractMin()
        node = graph.get(node_from)

        for neighbor, weight in node.edges:
            weight_sum = total_weight + weight

            if cost[neighbor.value][0] == -1:
                result.insertEdge([((node_from, neighbor.value), weight)])
                cost[neighbor.value] = [weight_sum, node_from]
                heap.insert(weight_sum, neighbor.value)

            if cost[neighbor.value][0] > weight_sum:
                result.insertEdge([((node_from, neighbor.value), weight)])
                result.deleteEdge([((neighbor.value, cost[neighbor.value][1]), cost[neighbor.value][0])])
                cost[neighbor.value] = [weight_sum, node_from]
                heap.insert(weight_sum, neighbor.value)

    return result


edges = [
    ((0, 3), 5),
    ((0, 2), 6),
    ((0, 1), 10),
    ((3, 5), 13),
    ((2, 1), 3),
    ((2, 5), 11),
    ((2, 4), 6),
    ((1, 5), 6),
    ((1, 4), 4),
    ((5, 6), 3),
    ((4, 6), 8),
]

weighted_graph = WeightedGraph(edges)

graph_matrix = weighted_graph.generateAdjacencyMatrix()
print("Adjacency Matrix:")
print(numpy.array(graph_matrix))

dijkstra_result = dijkstraGraph(weighted_graph, 0)
print("Dijkstra:")
print(numpy.array(dijkstra_result.generateAdjacencyMatrix()))

print(dijkstra_result)
