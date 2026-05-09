#  Chapter 03 Recursion — Lab Report 

## Student Information
- **Name:** [christiane Danielle Sidje]
- **Date:** [02/12/2026]
- **Course:** COSC 2436
## Recursion Concepts

### Two Parts of Every Recursive Function
1. Base Case: The condition that stops the recursion. It provides a direct answer without making another recursive call. Without it, the function would run forever.

2. Recursive Case: The part of the function where it calls itself with a smaller version of the problem until it eventually reaches the base case.

### The Call Stack
The call stack is a memory structure that keeps track of function calls. In recursion, each function call is placed on top of the stack and waits for the next call to finish. Once the base case is reached, the stack unwinds and returns values step by step.

Example using fact(4):

fact(4)
→ fact(3)
→ fact(2)
→ fact(1)
→ 1

Unwinding:
fact(1) = 1
fact(2) = 2 × 1 = 2
fact(3) = 3 × 2 = 6
fact(4) = 4 × 6 = 24

## Function Analysis

Function         | Base Case     | Recursive Case                     | Time Complexity
----------------|--------------|-------------------------------------|----------------
countdown       | i <= 0        | countdown(i - 1)                   | O(n)
fact            | x <= 1        | x * fact(x - 1)                   | O(n)
recursive_sum   | empty list    | first + recursive_sum(rest)       | O(n^2)
recursive_count | empty list    | 1 + recursive_count(rest)         | O(n^2)
recursive_max   | single item   | max(first, recursive_max(rest))   | O(n^2)

## Reflection Questions

1. What happens if you forget the base case?
The function will keep calling itself forever until the program crashes due to a stack overflow error.

2. Why is the naive Fibonacci implementation inefficient?
It recalculates the same values many times, leading to exponential time complexity O(2^n).

3. Draw the call stack for fact(4).

fact(4)
fact(3)
fact(2)
fact(1)

Then returns:
fact(1)=1
fact(2)=2
fact(3)=6
fact(4)=24atives like index-based recursion.

## challenges Encountered

One challenge in this lab was understanding how recursive functions repeatedly call themselves and how the program keeps track of those calls using the call stack. Tracing each recursive step carefully was important to avoid confusion about when functions stop and begin returning values. Another challenge was identifying proper base cases, since forgetting or incorrectly defining them can cause infinite recursion and program crashes. Practicing with examples like factorial and recursive list operations helped improve my understanding of how recursion breaks large problems into smaller ones
