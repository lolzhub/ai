
#selection sort
def selectionSort(arr):
    for i in range(len(arr)):
        min = float('-inf')
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j], arr[i]
    return arr
n = int(input("Enter number of elements : "))
arr = list()
for i in range(n):
    arr.append(int(input("Enter element {} : ".format(i+1))))
print("The sorted array is : ")
print(selectionSort(arr))


# Python program for Job Scheduling Problem
def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[1])  # Sort jobs based on their finish time
    n = len(jobs)
    result = [jobs[0]]

    for i in range(1, n):
        if jobs[i][0] >= result[-1][1]:
            result.append(jobs[i])

    return result

# Example usage
jobs = [(1, 3), (2, 5), (4, 7), (6, 9), (8, 10)]
schedule = job_scheduling(jobs)
print("Scheduled jobs:")
for job in schedule:
    print(f"Start Time: {job[0]}\tEnd Time: {job[1]}")



# Python program for Kruskal's algorithm to find Minimum Spanning Tree

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_mst(self):
        result = []
        self.edges.sort(key=lambda x: x[2])
        parent = []
        rank = []

        for v in range(self.num_vertices):
            parent.append(v)
            rank.append(0)

        i = 0
        e = 0

        while e < self.num_vertices - 1:
            u, v, weight = self.edges[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append((u, v, weight))
                self.union(parent, rank, x, y)

        return result

# # Example usage
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

mst = g.kruskal_mst()
print("Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"Edge: {u} - {v}\tWeight: {weight}")





# Single-Source Shortest Path Problem using Dijkstra's algorithm

# Function to find the vertex with the minimum distance value
def min_distance(distances, visited):
    min_dist = float('inf')
    min_vertex = None
    for v in range(len(distances)):
        if not visited[v] and distances[v] < min_dist:
            min_dist = distances[v]
            min_vertex = v
    return min_vertex

# Function to print the shortest path from source to destination
def print_path(parents, destination):
    if parents[destination] != -1:
        print_path(parents, parents[destination])
    print(destination, end=" ")

# Dijkstra's algorithm to find the shortest path
def dijkstra(graph, source):
    num_vertices = len(graph)
    distances = [float('inf')] * num_vertices  # Initialize distances with infinity
    parents = [-1] * num_vertices  # Initialize parents with -1
    visited = [False] * num_vertices  # Initialize visited array

    distances[source] = 0  # Distance of source vertex from itself is always 0

    for _ in range(num_vertices - 1):
        u = min_distance(distances, visited)
        visited[u] = True  # type: ignore


        for v in range(num_vertices):
            if not visited[v] and graph[u][v] != 0 and distances[u] + graph[u][v] < distances[v]: # type: ignore
                distances[v] = distances[u] + graph[u][v] # type: ignore
                parents[v] = u # type: ignore

    # Print the shortest paths
    print("Shortest paths from source vertex:")
    for v in range(num_vertices):
        print(f"Vertex {v}: ", end="")
        print_path(parents, v)
        print(f"\nDistance: {distances[v]}")

# Example graph representation
graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]

source_vertex = 0  # Choose the source vertex

dijkstra(graph, source_vertex)



#Prims Algorithm    Minimum Spanning Tree

def prim_mst(graph):
    num_vertices = len(graph)
    mst = [None] * num_vertices
    key = [float('inf')] * num_vertices
    visited = [False] * num_vertices

    key[0] = 0
    mst[0] = -1

    for _ in range(num_vertices - 1):
        u = min_key(key, visited)
        visited[u] = True

        for v in range(num_vertices):
            if 0 < graph[u][v] < key[v] and not visited[v]:
                key[v] = graph[u][v]
                mst[v] = u

    return mst

# Helper function to find the vertex with the minimum key value
def min_key(key, visited):
    min_val = float('inf')
    min_idx = -1
    for v in range(len(key)):
        if not visited[v] and key[v] < min_val:
            min_val = key[v]
            min_idx = v
    return min_idx

# Example graph representation
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 4],
    [6, 8, 0, 0, 9],
    [0, 5, 4, 9, 0]
]

mst = prim_mst(graph)
print("Minimum Spanning Tree:")
for i in range(1, len(mst)):
    print(f"Edge: {mst[i]} - {i}\tWeight: {graph[i][mst[i]]}")
