

MatrixGraph = [
    [0, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 1],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0]
]

# array to represent adjacency list
Adjacencylist = [
    [2],
    [1, 3, 5],
    [4, 2],
    [3, 5, 6],
    [2, 4],
    [4]
]

# hashmap to represent adja list

AdjacencylistMap = {
    1: [2],
    2: [1, 3, 5],
    3: [4, 2],
    4: [3, 5, 6],
    5: [2, 4],
    6: [4]
}


def breathFirstSearch(root, graph):
    distance = {}
    for idx, _ in enumerate(graph):

        distance[idx+1] = float("inf")
    distance[root] = 0

    queue = [root]
    current = None

    while (len(queue) != 0):
        current = queue.pop(0)

        curConnected = graph[current-1]
        neighborIdx = []
        idx = curConnected.index(1) if 1 in curConnected else -1
        while (idx != -1):
            neighborIdx.append(idx)
            if 1 in curConnected[idx+1:]:
                idx = curConnected.index(1, idx + 1)
            else:
                idx = -1

        for j in range(len(neighborIdx)):

            index = neighborIdx[j] + 1
            if (distance[index] == float("inf")):
                distance[index] = distance[current] + 1
                queue.append(index)

    return distance


print(breathFirstSearch(1, MatrixGraph))
