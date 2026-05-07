# Chapter 09: Djikstra — Lab Report 

## Student Information
- **Name:** Christiane Danielle
- **Date:** May 7, 2026
- **Course:** COSC 2436

## Algorithm Summary
- **How it works:** Dijkstra’s Algorithm finds the shortest path between nodes in a weighted graph with non-negative edge weights. It repeatedly selects the unprocessed node with the smallest known cost and updates the costs of neighboring nodes if a shorter path is found.
- **Time complexity:** O(V²) using a linear scan, or O((V + E) log V) using a priority queue.
- **When to use it:** This algorithm is useful for shortest-path problems such as GPS navigation, network routing, and game pathfinding.

## Test Results

| Input | Result | Notes |
|---|---|---|
| A-B(1), A-C(4), B-C(2), B-D(6), C-D(3) | A → B → C → D | Shortest path from A to D |
| Start: A, End: D | Total Cost = 6 | Weighted undirected graph |

## Reflection Questions

1. **Why must all edge weights be non-negative in Dijkstra’s Algorithm?**  
   Dijkstra’s Algorithm assumes that once the shortest path to a node is finalized, it will not change later. Negative edge weights can create shorter paths afterward, causing incorrect results.

2. **Why are edges stored in both directions in this program?**  
   The graph is undirected, so travel between connected nodes must work both ways. Storing edges in both directions ensures the algorithm can correctly explore all possible paths.

3. **How does the parents dictionary help reconstruct the shortest path?**  
   The `parents` dictionary stores the previous node used to reach each node on the shortest path. By tracing backward from the destination node to the start node, the full path can be rebuilt and then reversed into the correct order.

## Challenges Encountered
One challenge was understanding how node costs update during each iteration of the algorithm. Tracing the algorithm step by step with a small graph helped make the process clearer. Another challenge was handling invalid input and preventing negative edge weights, which required additional input validation in the program.ning Dijkstra’s algorithm, so it returns None to show that no route was found.
