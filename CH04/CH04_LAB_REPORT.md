# Lab 04: Quicksort

## Student Information
- **Name:** Christiane Danielle
- **Date:** March 1, 2026

## Quicksort Concepts

### Divide and Conquer
Quicksort uses **divide-and-conquer** by breaking the array into smaller subarrays around a pivot. Each subarray is sorted recursively, and the results are combined. This way, a large sorting problem is solved by solving smaller problems and merging them.

### The Three Steps
1. **Choose pivot:** Select an element to compare others against (here we use the first element).  
2. **Partition:** Split the array into two lists:  
   - `less`: elements ≤ pivot  
   - `greater`: elements > pivot  
3. **Recurse and combine:** Sort `less` and `greater` recursively, then combine them with the pivot in the middle.

## Tracing Quicksort

### Trace: quicksort([3, 5, 2, 1, 4])

1. **Initial call:** `[3, 5, 2, 1, 4]`  
   - Pivot = 3  
   - less = [2, 1]  
   - greater = [5, 4]  

2. **Recurse on less = [2, 1]**  
   - Pivot = 2 → less = [1], greater = []  
   - Combine: `[1] + [2] + [] = [1, 2]`  

3. **Recurse on greater = [5, 4]**  
   - Pivot = 5 → less = [4], greater = []  
   - Combine: `[4] + [5] + [] = [4, 5]`  

4. **Combine all:** `[1, 2] + [3] + [4, 5] = [1, 2, 3, 4, 5]`

---

## Complexity Analysis

| Case | Time Complexity | Why? |
|------|----------------|------|
| Best | O(n log n) | Pivot splits array roughly in half each time, giving balanced recursion. |
| Average | O(n log n) | Random or mixed data usually produces reasonably balanced partitions. |
| Worst | O(n²) | Array is already sorted (or reverse sorted) and first-element pivot is chosen each time, producing very unbalanced partitions. |

---

## Reflection Questions

1. **What happens if the array is already sorted and you always pick the first element as pivot?**  
   - Each pivot is the smallest element, so partitions are unbalanced. The recursion depth becomes n, causing O(n²) runtime.

2. **How could you improve pivot selection to avoid worst-case performance?**  
   - Pick a **random pivot** or use the **median-of-three** method to reduce the chance of unbalanced partitions.

3. **How does quicksort compare to other sorting algorithms you know (e.g., bubble sort, merge sort)?**  
   - Quicksort is usually much faster than bubble sort (O(n²)) and similar to merge sort (O(n log n)). Unlike merge sort, it can sort in place with minimal extra memory.

4. **Why do we use `array[1:]` instead of `array` when building the less and greater lists?**  
   - `array[1:]` excludes the pivot. Including the pivot in the partitions would duplicate it and break the algorithm.
