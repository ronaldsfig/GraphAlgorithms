from graph import Graph

class WeightedGraph(Graph):
    def __init__(self, edges=None):
        if edges is None:
            edges = []
        self.nodes = []
        self.num_nodes = 0
        self.insertEdge(edges)

    def __repr__(self):
        return "\n".join(["{}: {}".format(node.value, [(neighbor[0].value, neighbor[1]) for neighbor in node.edges]) for node in self.nodes])

    def __str__(self):
        return self.__repr__()
    
    def deleteNode(self, value):
        node_to_delete = next((node for node in self.nodes if node.value == value), None)

        if node_to_delete:
            for neighbor, _ in node_to_delete.edges:
                neighbor.edges = [edge for edge in neighbor.edges if edge[0] != node_to_delete]
            self.nodes.remove(node_to_delete)
            self.num_nodes -= 1

    def insertEdge(self, edges):
        for (node_x_value, node_y_value), weight in edges:
            node_x = next(
                (node for node in self.nodes if node.value == node_x_value), None)
            node_y = next(
                (node for node in self.nodes if node.value == node_y_value), None)

            if not node_x:
                node_x = self.insertNode(node_x_value)
            if not node_y:
                node_y = self.insertNode(node_y_value)

            node_x.edges.append([node_y, weight])
            node_y.edges.append([node_x, weight])

        self.num_nodes = len(self.nodes)

    def deleteEdge(self, edges):
        for (node_x_value, node_y_value), _ in edges:
            node_x = next((node for node in self.nodes if node.value == node_x_value), None)
            node_y = next((node for node in self.nodes if node.value == node_y_value), None)

            if node_x and node_y:
                node_x.edges = [edge for edge in node_x.edges if edge[0] != node_y]
                node_y.edges = [edge for edge in node_y.edges if edge[0] != node_x]

    def get(self, value):
        return next((node for node in self.nodes if node.value == value), None)

    def generateAdjacencyMatrix(self):
        num_nodes = len(self.nodes)
        adjacency_matrix = [[int(0)] * num_nodes for _ in range(num_nodes)]

        node_index_mapping = {node: index for index, node in enumerate(self.nodes)}

        for node in self.nodes:
            node_index = node_index_mapping[node]
            adjacency_matrix[node_index][node_index] = 0

            for neighbor, weight in node.edges:
                neighbor_index = node_index_mapping[neighbor]
                adjacency_matrix[node_index][neighbor_index] = weight

        return adjacency_matrix
