import sys

class DijkstraMST:
    def __init__(self, graph, num_vertices):
        self.num_vertices = num_vertices
        self.graph = graph
        self.dist = [sys.maxsize] * num_vertices
        self.visited = [False] * num_vertices

    def dijkstra(self, start_vertex):
        for i in range(self.num_vertices):
            self.dist[i] = sys.maxsize
            self.visited[i] = False

        self.dist[start_vertex] = 0
        for _ in range(self.num_vertices - 1):
            u = self.min_distance(self.dist, self.visited)
            self.visited[u] = True

            for v in range(self.num_vertices):
                if not self.visited[v] and self.graph[u][v] != 0 and self.dist[u] != sys.maxsize and self.dist[u] + self.graph[u][v] < self.dist[v]:
                    self.dist[v] = self.dist[u] + self.graph[u][v]

        self.print_mst(start_vertex)

    @staticmethod
    def min_distance(dist, visited):
        min_dist = sys.maxsize
        min_index = -1

        for i in range(len(dist)):
            if not visited[i] and dist[i] <= min_dist:
                min_dist = dist[i]
                min_index = i

        return min_index

    def print_mst(self, start_vertex):
        print("Vertex \t Distance from Source")
        for i in range(self.num_vertices):
            print(i, "\t", self.dist[i])

if __name__ == "__main__":
    n = int(input("Enter the size of the graph: "))
    graph = []
    for _ in range(n):
        row = []
        for j in range(n):
            weight = int(input("Enter the weight {}->{} of the graph: ".format(_, j)))
            row.append(weight)
        graph.append(row)

    start_vertex = int(input("Enter the starting vertex of the graph: "))

    dijkstra = DijkstraMST(graph, n)
    dijkstra.dijkstra(start_vertex)
