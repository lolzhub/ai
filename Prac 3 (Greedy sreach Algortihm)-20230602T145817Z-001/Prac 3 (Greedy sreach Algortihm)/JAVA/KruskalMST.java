import java.util.*;

public class KruskalMST {
    
    class Edge implements Comparable<Edge> {
        int src, dest, weight;
        
        public int compareTo(Edge other) {
            return this.weight - other.weight;
        }
    }
    
    public void kruskal(int[][] graph, int numVertices) {

        List<Edge> edges = new ArrayList<>();
        for (int i = 0; i < numVertices; i++) {
            for (int j = i + 1; j < numVertices; j++) {
                if (graph[i][j] != 0) {
                    Edge edge = new Edge();
                    edge.src = i;
                    edge.dest = j;
                    edge.weight = graph[i][j];
                    edges.add(edge);
                }
            }
        }
        
        Collections.sort(edges);
 
        int[] parent = new int[numVertices];
        for (int i = 0; i < numVertices; i++) {
            parent[i] = i;
        }

        List<Edge> mst = new ArrayList<>();
        
        for (Edge edge : edges) {
            int srcParent = find(parent, edge.src);
            int destParent = find(parent, edge.dest);
            if (srcParent != destParent) {
                mst.add(edge);
                parent[srcParent] = destParent;
            }
        }
        int sum=0;
        System.out.println("Edges in the MST:");
        for (Edge edge : mst) {
            System.out.println(edge.src + " - " + edge.dest + " : " + edge.weight);
            sum+=edge.weight;
        }
        System.out.println("Minimum weight of MST: " + sum);
    }
    
    private int find(int[] parent, int i) {
        if (parent[i] != i) {
            parent[i] = find(parent, parent[i]);
        }
        return parent[i];
    }
    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter the  size of the graph: ");
        int n = in.nextInt();
        int[][] graph = new int[n][n];
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                System.out.print("Enter the weight "+i+ "-> "+j+" of the graph: ");
                graph[i][j]=in.nextInt();
            }
        }
        KruskalMST kruskal = new KruskalMST();
        kruskal.kruskal(graph, n);
    }
}
