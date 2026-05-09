#  Chap 10: Truck Packing - Lab Report
## Student Information
**Name:** [Christiane Danielle]  
**Date:** [04/19/2026]  
**Algorithm Analysis:** Greedy Truck Packing Algorithm  

---
## Algorithm Understanding

**What type of problem is this algorithm solving?**
Optimization / approximation problem (specifically a packing problem similar to bin-packing or knapsack)

**Is this greedy algorithm guaranteed to produce the optimal solution? Why or why not?**
No, it is not guaranteed to be optimal. Greedy algorithms make locally optimal choices (choosing the largest box first), but this can prevent better overall combinations of smaller boxes that would use space more efficiently.

**What is the greedy choice made in this algorithm?**
Always selecting the largest available box (by volume) that still fits in the remaining truck space.

## Implementation Questions

**1.Why do we sort the boxes in descending order of volume before packing?**
To prioritize placing larger boxes first, since they are harder to fit later. This aims to reduce the chance of leaving large unused space that smaller boxes cannot fill efficiently.

**2.What would happen if we sorted the boxes in ascending order instead?**
Smaller boxes would be packed first, which might fill the space inefficiently and leave no room for larger boxes, potentially leading to worse overall space utilization.

**3.Why do we keep track of used_volume?**
To ensure we do not exceed the truck’s total capacity and to track how much space remains while deciding whether a new box can be added.

## Extension: Dimension Constraints

**1.Why is checking only volume not sufficient for real-world packing?**
Because physical objects must fit within actual dimensions (length, width, height). Even if the volume fits, the shape or orientation of the box may prevent it from fitting inside the truck.

**2.Give an example where a box fits by volume but not by dimensions.**
A truck has dimensions 10×10×10 (volume 1000). A box has dimensions 20×5×5 (volume 500). Although the volume is smaller than the truck’s, the box cannot fit because its length (20) exceeds the truck’s length (10).

**3.How would you modify the algorithm to check dimension constraints before packing a box?**
Before adding a box, check that its length, width, and height are each less than or equal to the corresponding truck dimensions (possibly considering rotations). Only pack the box if it satisfies these constraints in addition to the volume check.

## Reflection Questions

**1.What is a limitation of this greedy approach? Provide a scenario where it fails to find the optimal solution.
It may miss better combinations. For example, if the truck volume is 100 and boxes are 60, 50, and 50: the greedy algorithm picks 60 first (remaining space 40), so no other box fits (total = 60). But the optimal solution is 50 + 50 = 100.**

**2.How is this problem related to the Knapsack Problem?**
It is similar to the knapsack problem where items (boxes) have sizes (volumes) and must fit within a capacity (truck volume). The goal is to maximize utilization, just like maximizing value in knapsack.

**3.What type of algorithm would guarantee an optimal solution for this problem? What is the tradeoff?**
A dynamic programming or exhaustive search (backtracking) approach would guarantee an optimal solution. The tradeoff is much higher computational cost (time and sometimes memory), especially for large numbers of boxes.

**4.If the truck had weight limits in addition to volume, how would the algorithm need to change?**
Each box would also have a weight, and the algorithm would need to track both total volume and total weight. A box would only be added if it satisfies both constraints, making it a multi-constraint knapsack problem.

**5.Why are greedy algorithms often preferred despite not always being optimal?**
They are simple to implement, run very fast, and often produce good enough solutions in practice, especially when exact optimality is not required.

## Challenges Encountered

One challenge in this lab was understanding the limitations of the greedy approach, especially how choosing the largest box first can sometimes lead to suboptimal packing results. It was important to work through examples step by step to see how early decisions affect the remaining space. Another challenge was recognizing why volume alone is not enough to determine whether a box fits, since real-world constraints like dimensions can change whether a box can actually be placed. Translating these ideas into algorithm logic helped reinforce the difference between approximate solutions and optimal solutions.
