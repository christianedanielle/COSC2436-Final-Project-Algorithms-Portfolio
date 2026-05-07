# Hash Table Lab Report

## Student Information
- Name: Christiane Danielle Sidje
- Date: 02/12/2026

---

# Key Concepts

## What is a Hash Table?

A hash table stores data using key-value pairs.

A hash function converts a key into an index in an array.

Example:

hash("apple") = 2

The value "apple" is stored at index 2.

Hash tables are efficient because insert and search operations are usually O(1).

---

## What is Linear Probing?

Linear probing is a collision handling method.

If two keys hash to the same index:
1. Check the next index
2. Continue until an empty spot is found

Example:

"apple" -> index 2  
"banana" -> index 2

Index 2 is occupied, so place "banana" at index 3.

---

# Tracing Exercise

## Table Size = 5

## Insert "apple"

hash("apple") = 2

| Index | Value |
|---|---|
| 0 | |
| 1 | |
| 2 | apple |
| 3 | |
| 4 | |

---

## Insert "banana"

hash("banana") = 2

Collision at index 2.

Linear probing:
- index 2 occupied
- index 3 empty

| Index | Value |
|---|---|
| 0 | |
| 1 | |
| 2 | apple |
| 3 | banana |
| 4 | |

---

## Insert "orange"

hash("orange") = 4

| Index | Value |
|---|---|
| 0 | |
| 1 | |
| 2 | apple |
| 3 | banana |
| 4 | orange |

---

# Complexity Analysis

| Operation | Average Case | Worst Case |
|---|---|---|
| Insert | O(1) | O(n) |
| Search | O(1) | O(n) |

## Explanation

Average case is O(1) because hashing is fast.

Worst case is O(n) when many collisions happen.

---

# Reflection Questions

## 1. What are the advantages of using a hash table?

- Fast insertion
- Fast searching
- Efficient storage
- Useful for dictionaries and databases

## 2. How does the hash function affect performance?

A good hash function spreads data evenly across the table.

This reduces collisions and improves speed.

A bad hash function creates many collisions and slows down operations.


## 3. What are other collision resolution techniques besides linear probing?

- Quadratic probing
- Double hashing
- Separate chaining


