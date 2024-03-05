class Graph:
    class Node:
        def __init__(self, value):
            self.value = value
            self.edges = []

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
        new_node = self.Node(value)
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

# Exemplo de uso:
edges_iniciais = [(1, 2), (2, 3), (3, 4)]
grafo = Graph(edges_iniciais)

# Imprimindo a representação do grafo
print("Grafo inicial:")
print(grafo)

# Adicionando mais arestas
edges_adicionais = [(4, 5), (5, 6), (6, 1)]
grafo.insertEdge(edges_adicionais)

# Imprimindo a representação do grafo após a adição de arestas
print("\nGrafo após adição de arestas:")
print(grafo)

# Excluindo uma aresta
aresta_para_excluir = [(2, 3)]
grafo.deleteEdge(aresta_para_excluir)

# Imprimindo a representação do grafo após a exclusão de arestas
print("\nGrafo após exclusão de arestas:")
print(grafo)

# Excluindo um nó
no_para_excluir = 4
grafo.deleteNode(no_para_excluir)

# Imprimindo a representação do grafo após a exclusão de um nó
print("\nGrafo após exclusão de um nó:")
print(grafo)