#include <iostream>
#include <vector>
#include <limits>

class DijkstraMST {
private:
    int numVertices;
    std::vector<int> dist;
    std::vector<bool> visited;
    std::vector<std::vector<int>> graph;

public:
    DijkstraMST(const std::vector<std::vector<int>>& graph, int numVertices) {
        this->numVertices = numVertices;
        this->graph = graph;
        this->dist.resize(numVertices, std::numeric_limits<int>::max());
        this->visited.resize(numVertices, false);
    }

    void dijkstra(int startVertex) {
        for (int i = 0; i < numVertices; i++) {
            dist[i] = std::numeric_limits<int>::max();
            visited[i] = false;
        }

        dist[startVertex] = 0;
        for (int i = 0; i < numVertices - 1; i++) {
            int u = minDistance(dist, visited);

            visited[u] = true;

            for (int v = 0; v < numVertices; v++) {
                if (!visited[v] && graph[u][v] != 0 && dist[u] != std::numeric_limits<int>::max() && dist[u] + graph[u][v] < dist[v]) {
                    dist[v] = dist[u] + graph[u][v];
                }
            }
        }

        printMST(startVertex);
    }

private:
    int minDistance(const std::vector<int>& dist, const std::vector<bool>& visited) {
        int minDist = std::numeric_limits<int>::max();
        int minIndex = -1;

        for (int i = 0; i < numVertices; i++) {
            if (!visited[i] && dist[i] <= minDist) {
                minDist = dist[i];
                minIndex = i;
            }
        }

        return minIndex;
    }

    void printMST(int startVertex) {
        std::cout << "Vertex \t Distance from Source\n";
        for (int i = 0; i < numVertices; i++) {
            std::cout << i << "\t" << dist[i] << "\n";
        }
    }
};

int main() {
    int n;
    std::cout << "Enter the size of the graph: ";
    std::cin >> n;

    std::vector<std::vector<int>> graph(n, std::vector<int>(n));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            std::cout << "Enter the weight " << i << "->" << j << " of the graph: ";
            std::cin >> graph[i][j];
        }
    }

    DijkstraMST dijkstra(graph, n);

    int startVertex;
    std::cout << "Enter the starting vertex of the graph: ";
    std::cin >> startVertex;

    dijkstra.dijkstra(startVertex);

    return 0;
}

