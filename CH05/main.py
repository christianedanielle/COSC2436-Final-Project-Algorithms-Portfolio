
from typing import Any, Optional

class HashTable:
    """Basic hash table with linear probing for collision resolution."""

    def __init__(self, size: int):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key: Any) -> int:
        """Compute the hash index for a given key."""
        return hash(key) % self.size

    def insert(self, key: Any, value: Any) -> None:
        """Insert a key-value pair using linear probing if necessary."""
        index = self.hash_function(key)
        start_index = index

        while self.table[index] is not None:
            # If key already exists, update value
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size
            if index == start_index:
                raise Exception("Hash table is full!")

        self.table[index] = (key, value)

    def search(self, key: Any) -> Optional[Any]:
        """Search for a key and return its value, or None if not found."""
        index = self.hash_function(key)
        start_index = index

        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == start_index:
                return None
        return None


# Example usage:
if __name__ == "__main__":
    ht = HashTable(10)
    ht.insert("a", 100)
    ht.insert("b", 200)
    ht.insert("c", 300)

    print(ht.search("a"))  # 100
    print(ht.search("b"))  # 200
    print(ht.search("c"))  # 300
    print(ht.search("d"))  # None
