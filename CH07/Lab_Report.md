LAB REPORT 07 : Binary Trees

------------------------------------------------------------
Student Information
------------------------------------------------------------
Name: Christiane Danieele
Date: 03/29/2026
Course: COSC 2436

------------------------------------------------------------
Algorithm Summary
------------------------------------------------------------

Binary Search Tree (BST)
A Binary Search Tree is a hierarchical data structure where each node
has at most two children. For every node:
- Left subtree values are smaller than the node
- Right subtree values are larger than the node

This structure allows efficient searching, insertion, and traversal.

- Average Search Time (balanced): O(log n)
- Worst Case Search Time (unbalanced): O(n)

BSTs are commonly used in databases, searching systems, and sorted data
storage where fast lookup is needed.

------------------------------------------------------------
Test Results
------------------------------------------------------------

Inserted Values:
[7, 3, 9, 1, 5]

Tree Structure (conceptual):
        7
      /   \
     3     9
    / \
   1   5

Inorder Traversal Output:
[1, 3, 5, 7, 9]

Search Results:
- Search 5  → True
- Search 10 → False
- Search in empty tree → False

------------------------------------------------------------
Code Implementation
------------------------------------------------------------

from typing import Optional, List

class Node:
    def __init__(self, data: int):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class BinaryTree:
    def __init__(self):
        self.root: Optional[Node] = None

    # Insert method
    def insert(self, data: int) -> None:
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, current: Node, new_node: Node) -> None:
        if new_node.data < current.data:
            if current.left is None:
                current.left = new_node
            else:
                self._insert_recursive(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insert_recursive(current.right, new_node)

    # Inorder traversal
    def inorder_traversal(self) -> List[int]:
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node: Optional[Node], result: List[int]) -> None:
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)

    # Search method
    def search(self, data: int) -> bool:
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node: Optional[Node], data: int) -> bool:
        if node is None:
            return False
        if node.data == data:
            return True
        elif data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)


# Test cases (main section)
if __name__ == "__main__":
    tree = BinaryTree()

    values = [7, 3, 9, 1, 5]
    for v in values:
        tree.insert(v)

    print("Inorder Traversal:", tree.inorder_traversal())
    print("Search 5:", tree.search(5))
    print("Search 10:", tree.search(10))

    empty_tree = BinaryTree()
    print("Search in empty tree:", empty_tree.search(1))

------------------------------------------------------------
Reflection Questions
------------------------------------------------------------

1. Why does inorder traversal give sorted output?
Because the BST property ensures left < root < right. Inorder traversal
visits nodes in that exact order, producing sorted output.

2. What makes the search operation efficient in a BST?
Each comparison eliminates half of the remaining tree (in a balanced BST),
reducing time complexity to O(log n).

3. What happens when the tree becomes unbalanced?
It becomes similar to a linked list, causing search and insertion to degrade
to O(n) time.

------------------------------------------------------------
Challenges Encountered
------------------------------------------------------------

The main challenge was understanding how recursion works in both insertion
and search methods. Tracing the function calls step-by-step helped clarify
how nodes are placed and found in the tree. Another challenge was visualizing
how the tree structure changes after each insertion, which improved after
drawing the tree manually.
------------------------------------------------------------

Another challenge was distinguishing BFS from DFS in practice.
Using step-by-step examples and visualizing traversal paths made
it clearer when to use queues versus recursion.
------------------------------------------------------------shing between BFS and DFS in practical terms. Reviewing small tree examples step by step and visualizing the traversal order helped make the differences clearer, especially regarding when to use a queue versus recursion.
