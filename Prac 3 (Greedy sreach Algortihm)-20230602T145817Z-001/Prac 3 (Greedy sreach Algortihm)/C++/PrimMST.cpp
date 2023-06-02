#include <iostream>
#include <vector>
#include <climits>

int minKey(const std::vector<int>& key, const std::vector<bool>& mstSet) {
    int min = INT_MAX, minIndex = -1;

    for (int i = 0; i < key.size(); i++) {
        if (mstSet[i] == false && key[i] < min) {
            min = key[i];
            minIndex = i;
        }
    }

    return minIndex;
}

void printMST(const std::vector<int>& parent, const std::vector<std::vector<int>>& graph, int sum) {
    std::cout << "Edge \tWeight\n";
    for (int i = 1; i < parent.size(); i++) {
        std::cout << parent[i] << " - " << i << "\t" << graph[i][parent[i]] << "\n";
    }
    std::cout << "Minimum weight of MST: " << sum << "\n";
}

void prim(const std::vector<std::vector<int>>& graph, int numVertices) {
    std::vector<int> parent(numVertices);
    std::vector<int> key(numVertices);
    std::vector<bool> mstSet(numVertices);

    for (int i = 0; i < numVertices; i++) {
        key[i] = INT_MAX;
        mstSet[i] = false;
    }

    key[0] = 0;
    parent[0] = -1;

    for (int count = 0; count < numVertices - 1; count++) {
        int u = minKey(key, mstSet);
        mstSet[u] = true;

        for (int v = 0; v < numVertices; v++) {
            if (graph[u][v] != 0 && mstSet[v] == false && graph[u][v] < key[v]) {
                parent[v] = u;
                key[v] = graph[u][v];
            }
        }
    }

    int sum = 0;
    for (int i = 0; i < numVertices; i++) {
        sum += key[i];
    }

    printMST(parent, graph, sum);
}

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

    // Example graph
    // std::vector<std::vector<int>> graph = {
    //     {0, 2, 0, 6, 0},
    //     {2, 0, 3, 8, 5},
    //     {0, 3, 0, 0, 7},
    //     {6, 8, 0, 0, 9},
    //     {0, 5, 7, 9, 0}
    // };

    prim(graph, n);

    return 0;
}

