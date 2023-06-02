#include <iostream>
#include <list>
#include <vector>

class Graph {
private:
    int V;
    std::vector<std::list<int>> adj;

public:
    Graph(int v) {
        V = v;
        adj.resize(v);
    }

    void addEdge(int v, int w) {
        adj[v].push_back(w);
    }

    void DFS(int v) {
        std::vector<bool> visited(V, false);
        DFSUtil(v, visited);
    }

private:
    void DFSUtil(int vertex, std::vector<bool>& visited) {
        visited[vertex] = true;
        std::cout << vertex << " ";

        for (int a : adj[vertex]) {
            if (!visited[a]) {
                DFSUtil(a, visited);
            }
        }
    }
};

int main() {
    int n;
    std::cout << "Enter the size of the graph: ";
    std::cin >> n;

    Graph g(n);

    int size;
    std::cout << "Enter the size of input: ";
    std::cin >> size;

    for (int i = 0; i < size; i++) {
        std::cout << "Enter edges " << (i + 1) << " of graph: ";
        int j, k;
        std::cin >> j >> k;

        if (j < n && k < n) {
            g.addEdge(j, k);
        } else {
            std::cout << "Invalid Input\n";
        }
    }

    int start;
    std::cout << "Enter the starting vertex: ";
    std::cin >> start;

    std::cout << "DFS of Graph\n";
    g.DFS(start);

    return 0;
}

