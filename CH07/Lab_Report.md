Lab Report 07: Binary Trees
Student Information
Name: [Christiane Danielle]
LAB REPORT

------------------------------------------------------------
Student Information
------------------------------------------------------------
Name: Christiane Danieele
Date: 03/29/2026

------------------------------------------------------------
Algorithm Analysis
------------------------------------------------------------

Binary Search Tree (BST)
- Search Time (balanced): O(log n)
- Search Time (unbalanced): O(n)
- BST Property:
  A binary search tree maintains the property that for each node,
  all elements in the left subtree are less than the node, and all
  elements in the right subtree are greater.

------------------------------------------------------------
Traversals
------------------------------------------------------------

Preorder Traversal:  Root, Left, Right
Use Case: Copying a tree

Inorder Traversal:   Left, Root, Right
Use Case: Getting sorted elements

Postorder Traversal: Left, Right, Root
Use Case: Deleting a tree

------------------------------------------------------------
Reflection Questions
------------------------------------------------------------

1. Why does inorder traversal give sorted output?
Inorder traversal visits nodes in the order Left → Root → Right.
In a BST, left nodes are smaller and right nodes are larger, so
this naturally produces sorted order.

2. When would a BST become unbalanced?
A BST becomes unbalanced when values are inserted in sorted or
nearly sorted order, causing it to degrade into a structure similar
to a linked list.

3. What's the difference between BFS and DFS for trees?
BFS (Breadth-First Search) explores level by level using a queue.
DFS (Depth-First Search) explores as deep as possible along each
branch before backtracking, typically using recursion or a stack.

------------------------------------------------------------
Challenges Encountered
------------------------------------------------------------

The main challenge was understanding how insertion order affects
the balance of a BST. Working through examples with sorted versus
random data helped show how a tree can become skewed.

Another challenge was distinguishing BFS from DFS in practice.
Using step-by-step examples and visualizing traversal paths made
it clearer when to use queues versus recursion.
------------------------------------------------------------shing between BFS and DFS in practical terms. Reviewing small tree examples step by step and visualizing the traversal order helped make the differences clearer, especially regarding when to use a queue versus recursion.
