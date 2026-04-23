from z3 import Solver, Int, And, Distinct, sat

# Create a 9x9 Sudoku grid of integer variables
def create_grid():
    return [[Int(f"x_{i}_{j}") for j in range(9)] for i in range(9)]

# Add Sudoku constraints to the solver
def add_constraints(s, grid):
    # Each cell is between 1 and 9
    for i in range(9):
        for j in range(9):
            s.add(And(grid[i][j] >= 1, grid[i][j] <= 9))

    # Rows must have distinct values
    for i in range(9):
        s.add(Distinct(grid[i]))

    # Columns must have distinct values
    for j in range(9):
        s.add(Distinct([grid[i][j] for i in range(9)]))

    # 3x3 subgrids must have distinct values
    for box_row in range(3):
        for box_col in range(3):
            cells = []
            for i in range(3):
                for j in range(3):
                    cells.append(grid[3*box_row + i][3*box_col + j])
            s.add(Distinct(cells))

# Apply a puzzle (0 = empty)
def add_puzzle(s, grid, puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] != 0:
                s.add(grid[i][j] == puzzle[i][j])

# Solve and print the Sudoku
def solve_sudoku(puzzle):
    s = Solver()
    grid = create_grid()

    add_constraints(s, grid)
    add_puzzle(s, grid, puzzle)

    if s.check() == sat:
        m = s.model()
        solution = [[m.evaluate(grid[i][j]).as_long() for j in range(9)] for i in range(9)]
        print("Solved Sudoku:")
        for row in solution:
            print(row)
        print()
    else:
        print("No solution found")

# Example puzzles
puzzle1 = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

puzzle2 = [
    [0,0,0,2,6,0,7,0,1],
    [6,8,0,0,7,0,0,9,0],
    [1,9,0,0,0,4,5,0,0],
    [8,2,0,1,0,0,0,4,0],
    [0,0,4,6,0,2,9,0,0],
    [0,5,0,0,0,3,0,2,8],
    [0,0,9,3,0,0,0,7,4],
    [0,4,0,0,5,0,0,3,6],
    [7,0,3,0,1,8,0,0,0]
]

puzzle3 = [
    [0,2,0,6,0,8,0,0,0],
    [5,8,0,0,0,9,7,0,0],
    [0,0,0,0,4,0,0,0,0],
    [3,7,0,0,0,0,5,0,0],
    [6,0,0,0,0,0,0,0,4],
    [0,0,8,0,0,0,0,1,3],
    [0,0,0,0,2,0,0,0,0],
    [0,0,9,8,0,0,0,3,6],
    [0,0,0,3,0,6,0,9,0]
]

if __name__ == "__main__":
    print("Puzzle 1:")
    solve_sudoku(puzzle1)

    print("Puzzle 2:")
    solve_sudoku(puzzle2)

    print("Puzzle 3:")
    solve_sudoku(puzzle3)
