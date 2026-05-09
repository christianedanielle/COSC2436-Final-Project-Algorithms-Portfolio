## Lab 08: Balanced Trees -Lab Report

------------------------------------------------------------
Student Information
------------------------------------------------------------
Name: Christiane Danielle
Date: 03/04/2026
Course: COSC 2436

------------------------------------------------------------
Algorithm Summary
------------------------------------------------------------

An AVL Tree is a self-balancing Binary Search Tree that automatically
keeps its height balanced after every insertion using rotations.

Each node stores a height value, and the balance factor is calculated as:
height(left subtree) - height(right subtree)

- Balance Factor Range: [-1, 0, 1]
- Time Complexity (all operations): O(log n)

If the tree becomes unbalanced, rotations (LL, RR, LR, RL) are applied
to restore balance while maintaining BST ordering rules.

AVL trees are used when fast and consistent search, insertion, and deletion
are required, especially in databases and indexing systems.

------------------------------------------------------------
Test Results
------------------------------------------------------------

Inserted values:
10, 20, 5, 4, 15

Final Inorder Traversal Output:
[4, 5, 10, 15, 20]

Observations:
- Tree remains balanced after each insertion
- Inorder traversal always returns sorted order
- Rotations are triggered automatically when imbalance occurs

------------------------------------------------------------
Reflection Questions
------------------------------------------------------------

**1. Why does an AVL tree need to maintain balance?**
To ensure operations such as search, insert, and delete stay efficient
at O(log n) instead of degrading to O(n) like a linked list.

**2. What triggers a rotation in an AVL tree?**
A rotation is triggered when the balance factor of a node becomes less
than -1 or greater than 1 after insertion.

**3. How does AVL tree insertion differ from a normal BST?**
AVL insertion includes additional steps to check balance factors and
perform rotations if needed, while a normal BST does not rebalance.

------------------------------------------------------------
## Challenges Encountered
The main difficulty was understanding how rotations (LL, RR, LR, RL)
fix different imbalance cases while still preserving the BST property.
Tracing each insertion step-by-step helped clarify how balance is restored.
