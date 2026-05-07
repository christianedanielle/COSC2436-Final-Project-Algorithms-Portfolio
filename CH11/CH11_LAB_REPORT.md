# Chapter 11: Knapsack Dynamic Programming — Lab Report

## Student Information
- **Name:** Christiane Danielle Sidje
- **Date:** May 7, 2026
- **Course:** COSC 2436

## Algorithm Summary
- **How it works:** The Knapsack Dynamic Programming algorithm solves the 0/1 knapsack problem by building a grid of optimal solutions for smaller capacities and item combinations. For each item, the algorithm compares the value of including the item versus excluding it and stores the better solution in the grid.
- **Time complexity:** O(n × W), where `n` is the number of items and `W` is the capacity of the knapsack.
- **When to use it:** This algorithm is useful for optimization problems where the goal is to maximize value while staying within a weight or capacity limit.

## Test Results

| Input | Result | Notes |
|---|---|---|
| Capacity = 6 | Maximum Value = 35500 | Best valid solution found |
| Items: GUITAR, STEREO, LAPTOP, iPHONE, BOOK, GOLD BAR | GOLD BAR + iPHONE + GUITAR + LAPTOP | Highest-value combination |

### Sample Program Output

```text
                   1           2           3           4           5           6
GUITAR       $1500(G)   $1500(G)   $1500(G)   $1500(G)   $1500(G)   $1500(G)
STEREO       $1500(G)   $1500(G)   $1500(G)   $3000(S)   $4500(GS)  $4500(GS)
LAPTOP       $1500(G)   $1500(G)   $2000(L)   $3500(GL)  $4500(GS)  $5000(SL)
iPHONE       $2000(i)   $3500(Gi)  $3500(Li)  $4000(GLi) $5500(GSi) $6500(SLi)
BOOK         $2000(i)   $3500(Gi)  $3500(Li)  $4000(GLi) $5500(GSi) $6500(SLi)
GOLD BAR     $30000(G)  $32000(Gi) $33500(GL) $35000(GLi)$35500(GSi)$35500(GSi)
```

## Reflection Questions

1. **Why is dynamic programming more efficient than brute force for the knapsack problem?**  
   Dynamic programming stores solutions to smaller subproblems so they do not need to be recalculated repeatedly. This greatly reduces the number of operations compared to brute force, which checks every possible item combination.

2. **Why does the algorithm compare including and excluding each item?**  
   The algorithm must determine whether adding an item increases the total value without exceeding the capacity. Comparing both possibilities ensures the best solution is stored for every capacity level.

3. **What does each cell in the DP grid represent?**  
   Each grid cell represents the best possible item combination for a specific capacity using the first set of items considered so far. The grid gradually builds toward the optimal final solution.

## Challenges Encountered
One challenge was understanding how the DP grid updates solutions step by step for each item and capacity. Tracing the table manually helped clarify how previous solutions are reused. Another difficulty was formatting the output neatly so the values and item abbreviations aligned correctly in the displayed grid.
