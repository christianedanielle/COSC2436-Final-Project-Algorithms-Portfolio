# Chapter 02: Selection Sort — Lab Report
 **Name:** Christiane Danielle
- **Date:** 02-05-2026

### Algorithm Analysis

#### Selection Sort
- **Time Complexity:** O(n)^2
- **How it works:**Repeatedly finds the smallest element in the unsorted portion of the list and swaps it with the first unsorted element, gradually building a sorted portion at the front.

#### Arrays vs Linked Lists

| Operation | Array | Linked List | Why? |
|-----------|-------|-------------|------
| Read      |  O(1) |  0(n) | Arrays allow direct indexing, while linked lists require traversal |
| Insert    |  O(n)|  O(1)*|     Arrays may need shifting; linked lists just update pointers |
| Delete    |   O(n)  | O(1)*          | Arrays shift elements; linked lists update links  |

### Reflection Questions

1. Why is selection sort O(n²)?
Selection sort uses two nested loops. For each element in the list, it scans the remaining unsorted elements to find the smallest value. This results in roughly n + (n-1) + (n-2) + ... + 1 comparisons, which simplifies to O(n²).

2. When would you choose a linked list over an array?
You would choose a linked list when you need frequent insertions or deletions, especially in the middle of the data structure, since linked lists can handle these operations efficiently without shifting elements. They are also useful when the size of the data changes frequently, as linked lists do not require resizing like arrays.

3. Why does Python use arrays (lists) as the default sequence type?
Python uses lists as the default sequence type because they are flexible, dynamic, and easy to use for storing collections of items of varying sizes and types.

## Challenges Encountered

One challenge encountered in this lab was understanding how selection sort repeatedly searches through the unsorted portion of the list to find the smallest value. Tracing each pass of the algorithm required careful attention to how elements were compared and swapped. Another challenge was comparing arrays and linked lists, especially understanding why some operations are faster in one structure than the other. Practicing with examples and analyzing the time complexity of each operation helped strengthen my understanding of how data structures affect program performance.
