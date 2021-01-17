from array import *

nodeCount = 9


def findMinimumDistance(distance, sptSet):
    minDist = float("inf")
    for i in range(nodeCount):
        if (not sptSet[i]) and (distance[i] <= minDist):
            minDist = distance[i]
            minIndex = i
    return (minIndex)


def dijkstra(graph, srcNode):
    distance = sptSet = []
    for i in range(nodeCount):
        distance.append(float("inf"))
        sptSet.append(False)
    distance[srcNode] = 0

    for i in range(nodeCount - 1):
        uNode = findMinimumDistance(distance, sptSet)
        sptSet[i] = True
        for vNode in range(nodeCount):
            if (not sptSet[vNode]) and (graph[uNode][vNode]):
                if (distance[uNode] != float("inf")) and (
                    distance[uNode] + graph[uNode][vNode] < distance[vNode]
                ):
                    distance[vNode] = distance[uNode] + graph[uNode][vNode]

    print("\nDISTANCE OF DESTINATION FROM SOURCE\n")
    for i in range(nodeCount):
        print(i, "\t", distance[i], "\n")


graph = [
    [0, 6, 0, 0, 0, 0, 0, 8, 0],
    [6, 0, 8, 0, 0, 0, 0, 13, 0],
    [0, 8, 0, 7, 0, 6, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 6, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 13, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0],
]

srcNode = int(input("Which node is source node ? : "))

dijkstra(graph, srcNode)
