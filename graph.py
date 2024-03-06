class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []

class Graph:
    def __init__(self, edges=None):
        if edges is None:
            edges = []
        self.nodes = []
        self.insertEdge(edges)
    
    def __repr__(self):
        return "\n".join(["{}: {}".format(node.value, [neighbor.value for neighbor in node.edges]) for node in self.nodes])

    def __str__(self):
        return self.__repr__()

    def insertNode(self, value):
        new_node = Node(value)
        self.nodes.append(new_node)
        return new_node
    
    def deleteNode(self, value):
        node_to_delete = next((node for node in self.nodes if node.value == value), None)

        if node_to_delete:
            node_neighbors = (node for node in node_to_delete.edges)
            for neighbor in node_neighbors:
                neighbor.edges.remove(node_to_delete)
            self.nodes.remove(node_to_delete)

    def insertEdge(self, edges):
        for node_x_value, node_y_value in edges:
            node_x = next((node for node in self.nodes if node.value == node_x_value), None)
            node_y = next((node for node in self.nodes if node.value == node_y_value), None)

            if not node_x:
                node_x = self.insertNode(node_x_value)
            if not node_y:
                node_y = self.insertNode(node_y_value)

            node_x.edges.append(node_y)
            node_y.edges.append(node_x)

    def deleteEdge(self, edges):
        for node_x_value, node_y_value in edges:
            node_x = next((node for node in self.nodes if node.value == node_x_value), None)
            node_y = next((node for node in self.nodes if node.value == node_y_value), None)

            if node_x and node_y:
                node_x.edges.remove(node_y)
                node_y.edges.remove(node_x)