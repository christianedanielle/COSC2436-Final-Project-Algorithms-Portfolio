# Chapter 03 :[ Recursion] — Lab Report

## Student Information
- **Name:** [christiane Danielle Sidje]
- **Date:** [02/12/2026]
- **Course:** COSC 2436

## Algorithm Summary
- **How it works:**These recursive functions solve problems by breaking them into smaller versions of the same problem. Each function continues calling itself with a reduced input until it reaches a simple base case that stops the recursion.
- **Time complexity:** countdown: O(n)
fact: O(n)
recursive_sum: O(n²) (due to list slicing)
recursive_count: O(n²) (due to slicing)
recursive_max: O(n²) (due to slicing)
- **When to use it:** Recursion is best used when a problem can naturally be broken into smaller identical subproblems, such as mathematical calculations (factorials), processing lists, or exploring hierarchical structures like trees.

## Test Results
| Input                      | Result  | Notes                    |
| -------------------------- | ------- | ------------------------ |
| countdown(3)               | 3 2 1 0 | Prints correct countdown |
| fact(5)                    | 120     | Correct factorial result |
| recursive_sum([1,2,3])     | 6       | Correct sum              |
| recursive_count([1,2,3,4]) | 4       | Correct element count    |
| recursive_max([3,1,7,2])   | 7       | Correct maximum value    |


## Reflection Questions
1.What is a base case and why is it important?
A base case is the condition that stops recursion. Without it, the function would call itself forever and cause a stack overflow.

2.Why is recursion sometimes inefficient in Python?
Recursion can be inefficient because each function call adds overhead to the call stack, and operations like list slicing create additional memory usage.

3.How could recursive_sum or recursive_max be improved?
They could be improved by passing an index instead of slicing the list, which would reduce time complexity from O(n²) to O(n).
## Challenges Encountered
The main challenge was understanding how list slicing inside recursion increases time complexity. While the logic is simple, each slice creates a new list, which makes the functions less efficient. This was resolved by analyzing how data is copied at each recursive step and recognizing more efficient alternatives like index-based recursion.
