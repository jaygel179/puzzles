from sudoku_solver.sudoku import SudokuSolver

initial_board = [
    [0, 5, 8, 4, 0, 9, 0, 2, 0],
    [0, 0, 0, 0, 6, 0, 0, 8, 9],
    [2, 0, 1, 0, 3, 0, 7, 0, 0],
    [0, 0, 0, 0, 1, 3, 4, 0, 0],
    [3, 2, 0, 0, 8, 0, 9, 0, 1],
    [0, 7, 9, 0, 0, 0, 6, 0, 8],
    [0, 6, 0, 0, 0, 5, 8, 1, 7],
    [8, 1, 5, 7, 0, 0, 3, 0, 4],
    [0, 3, 0, 0, 9, 0, 2, 0, 0],
]

ss = SudokuSolver()
ss.add_board(initial_board)
ss.solve()
ss.print_board()
