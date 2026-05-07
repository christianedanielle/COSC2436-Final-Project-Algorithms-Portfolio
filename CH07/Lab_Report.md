LAB REPORT 07 : Binary Trees

Student Information
------------------------------------------------------------
Name: Christiane Danielle

Date: 03/29/2026

Course: COSC 2436

------------------------------------------------------------
Algorithm Summary
------------------------------------------------------------

Binary Search Tree (BST)
A Binary Search Tree is a structure where each node has at most two children.
For every node, values in the left subtree are smaller and values in the right
subtree are larger.

- Average Search Time (balanced): O(log n)
- Worst Case Search Time (unbalanced): O(n)

This structure is used for efficient searching, insertion, and sorting of data.

------------------------------------------------------------
Test Results
------------------------------------------------------------

Inserted values:
[7, 3, 9, 1, 5]

Inorder Traversal Output:
[1, 3, 5, 7, 9]

Search Results:
Search 5 → True
Search 10 → False
Search in empty tree → False

------------------------------------------------------------
Reflection Questions
------------------------------------------------------------

1. Why does inorder traversal give sorted output?
Because in a BST, left nodes are smaller and right nodes are larger.
Inorder traversal visits left → root → right, producing sorted order.

2. When does a BST become unbalanced?
A BST becomes unbalanced when values are inserted in sorted or nearly sorted order,
causing the tree to behave like a linked list.

3. What is the difference between BFS and DFS?
BFS explores level by level using a queue, while DFS explores as deep as possible
before backtracking using recursion or a stack.

------------------------------------------------------------
Challenges Encountered
------------------------------------------------------------

The main challenge was understanding how recursion works in insertion and search.
It was also difficult at first to visualize how the tree changes after each insertion,
but testing small examples helped clarify the behavior.
------------------------------------------------------------
