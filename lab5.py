import sys

def read_graph(filename):
    with open(filename, 'r') as f:
        graph = []
        for line in f:
            row = [int(num) for num in line.split()]
            graph.append(row)
        return graph

graph1 = read_graph('graph1.txt')
graph2 = read_graph('graph2.txt')

if len(graph1) != len(graph2) or any(len(row1) != len(row2) for row1, row2 in zip(graph1, graph2)):
    print("Not isomorphic")
    sys.exit()

for i, row1 in enumerate(graph1):
    for j, elem1 in enumerate(row1):
        elem2 = graph2[i][j]
        if (elem1 == 0) != (elem2 == 0):
            print("Not isomorphic")
            sys.exit()

print("Isomorphic")
