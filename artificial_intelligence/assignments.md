(c) 2026 Freek van den Berg. All rights reserved.

# Traditional Artifical Intelligence Assignments

## Sudoku solver
A Sudoku solver typically uses a backtracking algorithm that fills in empty cells one by one by trying numbers from 1 to 9 and checking whether each placement is valid according to Sudoku rules (no duplicates in the same row, column, or 3×3 subgrid). The solver scans the grid for an empty spot, tests possible values, and recursively continues this process; if it reaches a point where no number fits, it backtracks to the previous step and tries a different option. This systematic trial-and-error approach ensures that all possibilities are explored efficiently, guaranteeing a correct solution if one exists.

See [Sudoku Solver](/python/sudoku_solver.py)

## Connect4 AI
A Connect 4 AI typically works by simulating future moves and choosing the one that leads to the best outcome using algorithms like minimax combined with alpha-beta pruning. The AI evaluates the board by scoring positions based on factors such as potential winning lines, blocking the opponent, and controlling the center columns, then recursively explores possible moves several steps ahead to predict how the game might unfold. By alternating between maximizing its own advantage and minimizing the opponent’s chances, the AI selects the move that offers the highest strategic value while keeping computation efficient.

See [Connect4](/python/connect4.py)

## Map colouring (Australia)
Map coloring in Python is typically implemented as a constraint satisfaction problem (CSP), where regions are represented as nodes in a graph and edges indicate neighboring regions that cannot share the same color. A common approach uses backtracking, where the algorithm assigns a color to each region and recursively checks whether the assignment satisfies the constraint that no adjacent regions have the same color; if a conflict occurs, it backtracks and tries a different color. Python makes this easy to implement using dictionaries to store neighbors and simple functions to validate assignments, allowing clear and concise solutions to problems like the Australia map coloring example.

See [Map colouring](/python/mapcoloring.py)

## Grammar parsing
This code below uses NLTK to demonstrate grammar parsing by defining a context-free grammar (CFG) that describes how sentences are structured (e.g., a sentence consists of a noun phrase and a verb phrase). It then creates a ChartParser, which efficiently analyzes a given sentence—“the big dog saw a cat with a telescope”—by breaking it into words and applying the grammar rules to generate all valid parse trees. Because the grammar allows prepositional phrases to attach in different ways, the parser produces multiple trees, illustrating ambiguity in natural language. Finally, the code prints each parse tree in both text and visual formats, showing how the sentence can be interpreted structurally in different ways.

See [Grammar Parsing](/python/grammarparsing.py)

## Time scheduling
Timetable scheduling is a classic Constraint Satisfaction Problem (CSP) where you assign time slots (and often rooms) to events—like classes or exams—while satisfying constraints such as no student having two classes at the same time, no teacher being double-booked, and limited room availability.

See [Time Scheduling](/python/timescheduling.py)

