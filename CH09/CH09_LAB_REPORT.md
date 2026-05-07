Lab Report 09: Djikstra
Student Information

Name: [Christiane Danielle]
Date: [09/04/26]
Algorithm Analysis: Dijkstra's Algorithm

What type of graph does this program build? [Your answer — directed/undirected, weighted/unweighted]
Why must all edge weights be non-negative for Dijkstra's to work? [Your explanation]
Time Complexity (with simple array scan for min-node): O(?)
Time Complexity (with a min-heap/priority queue): O(?)
Core Data Structures

Structure	Variable Name	What It Stores
Adjacency dict	graph	
Cost table	costs	
Parent table	parents	
Visited list	processed	
Algorithm Trace

Given nodes A, B, C, D and edges A-B(1), A-C(4), B-C(2), B-D(6), C-D(3), trace Dijkstra's from A to D:

Iteration	Current Node	costs[A]	costs[B]	costs[C]	costs[D]	processed
Init	—					
1						
2						
3						
4						
Shortest path A to D: [Your answer]
Total cost: [Your answer]

Reflection Questions

Why does the algorithm initialize all node costs to infinity except the start node?  
 Dijkstra’s algorithm initializes all node costs to infinity to represent that no paths to those nodes are known yet, while the start node is set to 0 because it costs nothing to begin there. This ensures that any real path discovered during the algorithm will be smaller than infinity, allowing the algorithm to correctly update and track the shortest distances as it explores the graph.

Why do we store edges in both directions (graph[a][b] and graph[b][a])? What would break if we only stored one direction?  
We store edges in both directions because the graph is undirected, meaning you can travel between nodes both ways; storing graph[a][b] and graph[b][a] ensures the algorithm can move freely in either direction. If we only stored one direction, the graph would effectively become directed, and Dijkstra’s algorithm might fail to find valid paths—for example, it could get stuck or miss a shorter route simply because the reverse connection wasn’t recorded.

The find_lowest_cost_node() function scans all nodes linearly. How would using a priority queue (min-heap) improve performance, and why does it matter for large graphs?
Using a priority queue (min-heap) makes the algorithm faster because instead of checking every node to find the smallest cost, it automatically gives you the smallest one in logarithmic time. Right now, the program scans all nodes every time, which is slow for big graphs. With a heap, the overall time is much better, so it can handle large graphs more efficiently without taking too long.

If a negative edge weight were introduced (e.g., A-B with weight -3), explain how Dijkstra's algorithm could produce an incorrect result. What algorithm handles negative weights? 
If a negative edge weight were introduced (e.g., A-B with weight -3), explain how Dijkstra's algorithm could produce an incorrect result. What algorithm handles negative weights? 

How does the parents dictionary allow path reconstruction? Why do we reverse the path at the end?
If a negative edge weight is introduced, Dijkstra’s algorithm can give the wrong result because it assumes that once a node with the lowest cost is chosen, its cost is final. However, a negative edge could later create a shorter path to that same node, but the algorithm won’t revisit it to update the cost. This leads to incorrect results. The algorithm that can handle negative weights is the Bellman-Ford algorithm.
What happens when the source and destination are in disconnected components of the graph? How does the code detect this?  If the source and destination are in different disconnected parts of the graph, no path exists between them. The code detects this because the destination’s cost stays at infinity after running Dijkstra’s algorithm, so it returns None to show that no route was found.
