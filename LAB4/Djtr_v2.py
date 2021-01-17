'''
Author : Dhruv B kakadiya

'''
class Graph:
    def min_distance(self, dist, queue):
        minimum = float("Inf")
        min_index = -1
        for i in range(len(dist)):
            if ((dist[i] < minimum) and (i in queue)):
                minimum = dist[i]
                min_index = i
        return min_index

    # print path from source to all node reccursively
    def printPath(self, parent, j):
        if (parent[j] == -1):
            print(j)
            return
        self.printPath(parent, parent[j])
        print(j)

    # for printing solution for shortest path
    def printSolution(self, dist, parent):
        src = self.src
        print("Vertex \t\t\nSrc -> Des\tDistance\tNext Hop\tPath\t\t\tTotal Hops")
        for i in range(1, len(dist)):
            print("\n%d --> %d \t%d\t" % (src, i, dist[i]), end = "")
            if(dist[i] != float('inf')):
                temp_path = []
                temp_path_string = ""
                currentNode = i
                hop_count = 0
                while(currentNode != src and currentNode >= 0 ):
                    hop_count += 1
                    temp_path.insert(0, currentNode)
                    temp_path_string = str(currentNode) + " ->" +  temp_path_string
                    currentNode = parent[currentNode]
                if(i == src):
                    temp_path.insert(0, src)
                temp_path_string = str(src) + "->" + temp_path_string
                temp_path_string = temp_path_string[ : -2]
                print(f"Next Hop:{temp_path[0]}\t\t", temp_path_string, "\t\tTotal_Hops: ", hop_count)

    def dijkstra(self, graph, src):
        self.src = src
        row = len(graph)
        col = len(graph[0])
        dist = [float("Inf")] * row
        parent = [-1] * row
        dist[src] = 0
        queue = []
        for i in range(row):
            queue.append(i)
        while (queue):
            u = self.min_distance(dist,queue)
            queue.remove(u)
            for i in range(col):
                if ((graph[u][i]) and (i in queue)):
                    if (dist[u] + graph[u][i] < dist[i]):
                        dist[i] = dist[u] + graph[u][i]
                        parent[i] = u
        self.printSolution(dist,parent)

g= Graph()

graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]

# Print the solution
src = int(input("Enter the source node :"))
g.dijkstra(graph,src)