# PART 1 — helper function
# ---------------------------------------------------------------------------
def calculate_total_value(solution, items):
    total = 0
    for name in solution:
        for item_name, weight, value in items:
            if item_name == name:
                total += value
    return total


# ---------------------------------------------------------------------------
# PART 2 — fill the DP grid
# ---------------------------------------------------------------------------
def knapsack(items, capacity):
    n = len(items)
    grid = [[[] for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        item_name, weight, value = items[i - 1]
        for w in range(1, capacity + 1):
            if weight > w:
                # TODO 2
                grid[i][w] = grid[i-1][w]
            else:
                # TODO 3
                include_solution = grid[i-1][w-weight] + [item_name]
                exclude_solution = grid[i-1][w]

                # TODO 4
                include_value = calculate_total_value(include_solution, items)
                exclude_value = calculate_total_value(exclude_solution, items)

                # TODO 5
                if include_value > exclude_value:
                    grid[i][w] = include_solution
                else:
                    grid[i][w] = exclude_solution

    return grid


# ---------------------------------------------------------------------------
# PART 3 — pretty-print the grid
# ---------------------------------------------------------------------------
def display_grid(grid, items):
    n = len(items)
    capacity = len(grid[0]) - 1
    cell_width = 12

    # TODO 6
    header = ""
    for w in range(1, capacity + 1):
        header += str(w).rjust(cell_width)

    print(" " * cell_width + header)

    for i in range(1, n + 1):
        # TODO 7
        row = items[i-1][0].ljust(cell_width)

        for cell in grid[i][1:]:
            if cell:
                # TODO 8
                value = calculate_total_value(cell, items)
                letters = "".join([name[0] for name in cell])
                row += f"${value}({letters})".rjust(cell_width)
            else:
                # TODO 9
                row += " ".rjust(cell_width)

        print(row)


# ---------------------------------------------------------------------------
# PART 4 — run it
# ---------------------------------------------------------------------------
items = [
    ("GUITAR", 1, 1500),
    ("STEREO", 4, 3000),
    ("LAPTOP", 3, 2000),
    ("iPHONE", 1, 2000),
    ("BOOK", 2, 100),
    ("GOLD BAR", 1, 30000),
]

capacity = 6

# TODO 10
grid = knapsack(items, capacity)

# TODO 11
display_grid(grid, items)
