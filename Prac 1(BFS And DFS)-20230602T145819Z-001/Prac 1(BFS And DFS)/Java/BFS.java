import java.util.*;

class Graph
{   private int V; 
    private LinkedList<Integer> adj[];  
    public Graph(int v)
    {   
        V=v;
        adj = new LinkedList[v];
        for (int i = 0; i < v; ++i)
        {
          adj[i] = new LinkedList();
    	}
    }        
    void addEdge(int v, int w)
    {
        adj[v].add(w);                              
    }

    void BFS(int s) {
        boolean visited[] = new boolean[V];
        BFSUtil(s, visited);
    }

    void BFSUtil(int s, boolean visited[]) {
        LinkedList<Integer> queue = new LinkedList<Integer>();
        visited[s] = true;
        queue.add(s);

        while (queue.size() != 0) {
            s = queue.poll();
            System.out.print(s + " ");

            Iterator<Integer> i = adj[s].listIterator();
            while (i.hasNext()) {
                int n = i.next();
                if (!visited[n]) {
                    visited[n] = true;
                    queue.add(n);
                }
            }
        }
    }

}

class Main
{
    public static void main(String[] args)
    {
        Scanner in= new Scanner(System.in);
        System.out.print("Enter the size of the graph: ");
        int n = in.nextInt();
        System.out.print("Enter the size of input: ");
        int size=in.nextInt();
        Graph g=new Graph(n);
        for(int i=0;i<size;i++){
            System.out.print("Enter edges  "+(i+1)+ " of graph: ");
            int j=in.nextInt();
            int k=in.nextInt();
            if(j<n && k<n){
               g.addEdge(j, k);
            }
            else{
                System.out.println("Invalid Input");
            }
        }
        System.out.println("Enter the starting vertex: ");
        int start=in.nextInt();
        System.out.println("BFS of Graph");
        g.BFS(start);
    }
}
