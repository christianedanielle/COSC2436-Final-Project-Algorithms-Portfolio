Chapter 1: [Binary Search] — Lab Report

## Student Information
- **Name:** [Christiane Danielle]
- **Date:** [06/05/2026] 
- **Course:** COSC 2436

## Algorithm Summary
- **How it works:** Linear search checks each element in the list one by one until it finds the target value or reaches the end. Binary search improves efficiency by repeatedly dividing a sorted list in half, comparing the middle element to the target, and narrowing the search range until the value is found or no elements remain.
- **Time complexity:**Linear Search: O(n)
Binary Search: O(log n)
- **When to use it:**Use linear search for small or unsorted datasets. Use binary search when the data is sorted and you need faster performance on larger datasets.


## Test Results

| Input        | Result            | Notes |
|-------------|------------------|------|
| Search 1    | Found at index 0  | Fast for both, binary slightly faster |
| Search 64   | Found at index 63 | Linear takes longer as it scans halfway |
| Search 128  | Found at index 127| Worst case for linear search |
| Search 50   | Found at index 49 | Binary significantly faster |
| Search 100  | Found at index 99 | Binary uses much fewer steps |
| Search 25   | Found at index 24 | Linear quicker due to early position |
| Search 75   | Found at index 74 | Binary still faster overall |
| Search 10   | Found at index 9  | Linear relatively quick |
| Search 90   | Found at index 89 | Binary faster due to halving |
| Search 200  | Not found         | Linear checks all; binary exits quickly |        


## Reflection Questions

1.Why is binary search faster than linear search?
Binary search is faster because it eliminates half of the remaining elements with each step. Instead of checking every item, it quickly narrows down the possible location, resulting in far fewer comparisons.
2.What is a limitation of binary search?
Binary search only works on sorted data. If the data is not sorted, it must be sorted first, which adds extra time and may reduce its overall efficiency in some cases.
3.How does input size affect performance?
As the input size increases, linear search time grows directly with the number of elements. Binary search grows much more slowly because it depends on the logarithm of the input size, making it much more scalable.

## Challenges Encountered

