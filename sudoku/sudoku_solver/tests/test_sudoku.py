from unittest import TestCase

from sudoku_solver.sudoku import SudokuSolver


class TestSudokuSolver(TestCase):
    def test_empty_board(self):
        expected_output = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [7, 8, 9, 1, 2, 3, 4, 5, 6],
            [2, 1, 4, 3, 6, 5, 8, 9, 7],
            [3, 6, 5, 8, 9, 7, 2, 1, 4],
            [8, 9, 7, 2, 1, 4, 3, 6, 5],
            [5, 3, 1, 6, 4, 2, 9, 7, 8],
            [6, 4, 2, 9, 7, 8, 5, 3, 1],
            [9, 7, 8, 5, 3, 1, 6, 4, 2],
        ]

        ss = SudokuSolver()
        ss.solve()

        assert ss._board == expected_output

    def test_easy_baord(self):
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
        expected_output = [
            [6, 5, 8, 4, 7, 9, 1, 2, 3],
            [7, 4, 3, 1, 6, 2, 5, 8, 9],
            [2, 9, 1, 5, 3, 8, 7, 4, 6],
            [5, 8, 6, 9, 1, 3, 4, 7, 2],
            [3, 2, 4, 6, 8, 7, 9, 5, 1],
            [1, 7, 9, 2, 5, 4, 6, 3, 8],
            [9, 6, 2, 3, 4, 5, 8, 1, 7],
            [8, 1, 5, 7, 2, 6, 3, 9, 4],
            [4, 3, 7, 8, 9, 1, 2, 6, 5],
        ]

        ss = SudokuSolver()
        ss.add_board(initial_board)
        ss.solve()

        assert ss._board == expected_output

    def test_hard_baord(self):
        initial_board = [
            [3, 0, 7, 0, 0, 0, 0, 2, 0],
            [0, 0, 0, 0, 7, 0, 1, 0, 0],
            [8, 0, 0, 3, 2, 0, 0, 6, 0],
            [0, 7, 0, 0, 0, 0, 6, 8, 4],
            [0, 0, 0, 7, 0, 9, 0, 0, 0],
            [1, 8, 2, 0, 0, 0, 0, 5, 0],
            [0, 4, 0, 0, 1, 8, 0, 0, 6],
            [0, 0, 1, 0, 4, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 9, 0, 1],
        ]
        expected_output = [
            [3, 1, 7, 6, 9, 4, 8, 2, 5],
            [2, 6, 4, 8, 7, 5, 1, 9, 3],
            [8, 9, 5, 3, 2, 1, 4, 6, 7],
            [9, 7, 3, 1, 5, 2, 6, 8, 4],
            [4, 5, 6, 7, 8, 9, 3, 1, 2],
            [1, 8, 2, 4, 6, 3, 7, 5, 9],
            [7, 4, 9, 2, 1, 8, 5, 3, 6],
            [5, 3, 1, 9, 4, 6, 2, 7, 8],
            [6, 2, 8, 5, 3, 7, 9, 4, 1],
        ]

        ss = SudokuSolver()
        ss.add_board(initial_board)
        ss.solve()
        ss.print_board()

        assert ss._board == expected_output

    def test_expert_baord(self):
        initial_board = [
            [0, 9, 0, 0, 0, 0, 0, 0, 3],
            [0, 2, 7, 8, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 9, 0, 0, 0],
            [0, 0, 0, 0, 0, 4, 0, 0, 0],
            [3, 0, 0, 0, 5, 0, 4, 0, 0],
            [0, 7, 0, 0, 0, 0, 2, 0, 1],
            [0, 0, 8, 4, 0, 0, 9, 0, 0],
            [0, 0, 0, 7, 0, 0, 1, 5, 8],
            [6, 0, 0, 0, 2, 0, 0, 4, 0],
        ]
        expected_output = [
            [8, 9, 4, 6, 7, 2, 5, 1, 3],
            [5, 2, 7, 8, 3, 1, 6, 9, 4],
            [1, 6, 3, 5, 4, 9, 8, 7, 2],
            [9, 1, 6, 2, 8, 4, 7, 3, 5],
            [3, 8, 2, 1, 5, 7, 4, 6, 9],
            [4, 7, 5, 3, 9, 6, 2, 8, 1],
            [7, 3, 8, 4, 1, 5, 9, 2, 6],
            [2, 4, 9, 7, 6, 3, 1, 5, 8],
            [6, 5, 1, 9, 2, 8, 3, 4, 7],
        ]

        ss = SudokuSolver()
        ss.add_board(initial_board)
        ss.solve()

        assert ss._board == expected_output
