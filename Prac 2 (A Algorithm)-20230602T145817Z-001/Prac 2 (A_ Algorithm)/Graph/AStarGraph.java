import java.util.*;

class Node implements Comparable<Node> {
    int vertex;
    int fScore;

    public Node(int vertex, int fScore) {
        this.vertex = vertex;
        this.fScore = fScore;
    }

    @Override
    public int compareTo(Node other) {
        return Integer.compare(this.fScore, other.fScore);
    }
}

class Edge {
    int destination;
    int weight;

    public Edge(int destination, int weight) {
        this.destination = destination;
        this.weight = weight;
    }
}

class Graph {
    private int numVertices;
    private List<List<Edge>> adjList;

    public Graph(int numVertices) {
        this.numVertices = numVertices;
        adjList = new ArrayList<>(numVertices);
        for (int i = 0; i < numVertices; i++) {
            adjList.add(new ArrayList<>());
        }
    }

    public void addEdge(int source, int destination, int weight) {
        adjList.get(source).add(new Edge(destination, weight));
    }

    public List<Integer> aStarAlgorithm(int start, int goal, List<Integer> heuristic) {
        int[] g = new int[numVertices];
        int[] f = new int[numVertices];
        int[] parent = new int[numVertices];
        Arrays.fill(g, Integer.MAX_VALUE);
        Arrays.fill(f, Integer.MAX_VALUE);
        Arrays.fill(parent, -1);

        g[start] = 0;
        f[start] = heuristic.get(start);

        PriorityQueue<Node> openList = new PriorityQueue<>();
        openList.offer(new Node(start, f[start]));

        while (!openList.isEmpty()) {
            Node current = openList.poll();
            int currentVertex = current.vertex;

            if (currentVertex == goal) {
                return reconstructPath(parent, goal, g[goal]);
            }

            for (Edge neighbor : adjList.get(currentVertex)) {
                int neighborVertex = neighbor.destination;
                int tentativeG = g[currentVertex] + neighbor.weight;

                if (tentativeG < g[neighborVertex]) {
                    parent[neighborVertex] = currentVertex;
                    g[neighborVertex] = tentativeG;
                    f[neighborVertex] = g[neighborVertex] + heuristic.get(neighborVertex);
                    openList.offer(new Node(neighborVertex, f[neighborVertex]));
                }
            }
        }

        return new ArrayList<>();
    }

    private List<Integer> reconstructPath(int[] parent, int goal, int pathCost) {
        List<Integer> path = new ArrayList<>();
        int current = goal;
        while (current != -1) {
            path.add(current);
            current = parent[current];
        }
        Collections.reverse(path);
        System.out.println("Path cost: " + pathCost);
        return path;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter the size of the graph: ");
        int n = in.nextInt();
        Graph graph = new Graph(n);

        System.out.print("Enter the size of input: ");
        int size = in.nextInt();
        System.out.println("Enter edges of the graph:");
        for (int i = 0; i < size; i++) {
            System.out.print("Enter the value of " + (i + 1) + " edge and its weight: ");
            int j = in.nextInt();
            int k = in.nextInt();
            int w = in.nextInt();
            if (j < n && k < n) {
                graph.addEdge(j, k, w);
            } else {
                System.out.println("Invalid Input");
            }
        }

        List<Integer> heuristic = new ArrayList<>();
        System.out.println("Enter the heuristic values for the vertices of the graph:");
        for (int i = 0; i < n; i++) {
            System.out.print("Enter " + i + " vertex's heuristic value: ");
            int h = in.nextInt();
            heuristic.add(h);
        }

        System.out.print("Enter the starting vertex of the graph: ");
        int startVertex = in.nextInt();
        System.out.print("Enter the ending vertex of the graph: ");
        int goalVertex = in.nextInt();

        List<Integer> path = graph.aStarAlgorithm(startVertex, goalVertex, heuristic);
        if (!path.isEmpty()) {
            System.out.print("Optimal path found:");
            for (int vertex : path) {
                System.out.print(" " + vertex);
            }
            System.out.println();
        } else {
            System.out.println("Path not found!");
        }
    }
}
