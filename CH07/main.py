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


# ✅ Test cases (main section)
if __name__ == "__main__":
    tree = BinaryTree()

    # Insert elements
    values = [7, 3, 9, 1, 5]
    for v in values:
        tree.insert(v)

    # Test inorder traversal (should be sorted)
    print("Inorder Traversal:", tree.inorder_traversal())  # [1, 3, 5, 7, 9]

    # Test search
    print("Search 5:", tree.search(5))   # True
    print("Search 10:", tree.search(10)) # False

    # Test empty tree search
    empty_tree = BinaryTree()
    print("Search in empty tree:", empty_tree.search(1))  # False
