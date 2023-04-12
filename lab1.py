import networkx as nx
import matplotlib.pyplot as plt


with open('matrix.txt', 'r') as f:
    matrix = [[int(num) for num in line.split()] for line in f.readlines()]
A = nx.Graph()
A.add_nodes_from(range(len(matrix)))

# Додавання зважених ребер
for i in range(len(matrix)):
    for j in range(i + 1, len(matrix[i])):
        weight = matrix[i][j]
        if weight > 0:
            A.add_edge(i, j, weight=weight)

# Візуалізація графа
pos = nx.spring_layout(A)
edge_labels = nx.get_edge_attributes(A, "weight")
nx.draw_networkx_edge_labels(A, pos, edge_labels=edge_labels, font_color='green')
nx.draw(A, pos, with_labels=True)
plt.show()


def boruvka_mst(graph):

    mst = []

    n = len(graph)

    cheapest = [None] * n

    component = [i for i in range(n)]

    while len(set(component)) > 1:
        for i in range(n):
            min_edge = None
            for j in range(n):
                if graph[i][j] > 0 and component[i] != component[j]:
                    if min_edge is None or graph[i][j] < graph[min_edge[0]][min_edge[1]]:
                        min_edge = (i, j)
            cheapest[i] = min_edge

        for i, edge in enumerate(cheapest):
            if edge is not None:
                if component[edge[0]] != component[edge[1]]:
                    weight = graph[edge[0]][edge[1]]
                    mst.append((edge[0], edge[1], weight))
                    old_component = component[edge[1]]
                    new_component = component[edge[0]]
                    for j in range(n):
                        if component[j] == old_component:
                            component[j] = new_component
    return mst

mst = boruvka_mst(matrix)
for edge in mst:
    print(f"({edge[0]}, {edge[1]}) weight={edge[2]}")
