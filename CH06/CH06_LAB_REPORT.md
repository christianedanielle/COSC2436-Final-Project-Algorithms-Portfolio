# Lab 06: Breadth-First Search - Lab Report

## Student Information
- Name: Christiane Danielle Sidje
- Date: 02/19/2026

---

# Graph Concepts

## Adjacency List Representation

The graph is stored using an adjacency list.

Each city is a node, and every node keeps a list of connected neighboring cities.

Example:

Houston -> Dallas, Austin  
Dallas -> Houston, El Paso

This representation is efficient because it only stores existing connections between cities.

---

## BFS Algorithm Steps

1. Start at the source node
2. Mark the node as visited
3. Add the node to a queue
4. Remove the first node from the queue
5. Visit all unvisited neighboring nodes
6. Mark neighbors as visited
7. Add neighbors to the queue
8. Repeat until destination is found or queue is empty

---

# Test Results

| Start | End | Path | Edges |
|---|---|---|---|
| Houston | El Paso | Houston -> Dallas -> El Paso | 2 |
| Houston | McKinney | Houston -> Dallas -> McKinney | 2 |
| Dallas | Laredo | Dallas -> Austin -> Laredo | 2 |

---

# Reflection Questions

## 1. Why does BFS use a queue instead of a stack?

BFS uses a queue because it processes nodes in the order they are discovered.

This allows BFS to search level by level and guarantees the shortest path in an unweighted graph.

---

## 2. What's the difference between BFS shortest path and actual shortest distance?

BFS shortest path means the path with the fewest edges.

Actual shortest distance considers weighted values such as miles or travel time.

BFS does not account for edge weights.

---

## 3. When would you use BFS vs DFS?

Use BFS:
- Finding shortest paths
- Exploring nearby nodes first
- Level-order traversal

Use DFS:
- Exploring all possible paths
- Recursive problems
- Detecting cycles and connected components

---

# Program Summary

The program creates a Texas road network graph and demonstrates Breadth-First Search.

Main features:
- Builds a graph of connected Texas cities
- Finds shortest paths between cities using BFS
- Displays distances from Houston
- Demonstrates queue-based graph traversal

The program shows that BFS explores cities by distance level:
- Distance 1 first
- Distance 2 next
- Continues until destination is found

This guarantees the shortest path by number of edges.

---

