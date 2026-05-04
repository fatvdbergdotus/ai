(c) 2026 Freek van den Berg. All rights reserved.

# Artifical Intelligence Assignments

## Sudoku solver
A Sudoku solver typically uses a backtracking algorithm that fills in empty cells one by one by trying numbers from 1 to 9 and checking whether each placement is valid according to Sudoku rules (no duplicates in the same row, column, or 3×3 subgrid). The solver scans the grid for an empty spot, tests possible values, and recursively continues this process; if it reaches a point where no number fits, it backtracks to the previous step and tries a different option. This systematic trial-and-error approach ensures that all possibilities are explored efficiently, guaranteeing a correct solution if one exists.

See [Sudoku Solver](/python/sudoku_solver.py)

## Connect4 AI
A Connect 4 AI typically works by simulating future moves and choosing the one that leads to the best outcome using algorithms like minimax combined with alpha-beta pruning. The AI evaluates the board by scoring positions based on factors such as potential winning lines, blocking the opponent, and controlling the center columns, then recursively explores possible moves several steps ahead to predict how the game might unfold. By alternating between maximizing its own advantage and minimizing the opponent’s chances, the AI selects the move that offers the highest strategic value while keeping computation efficient.

See [Connect4](/python/connect4.py)
