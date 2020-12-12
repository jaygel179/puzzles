EMPTY_BOARD = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]


class SudokuSolver(object):
    def __init__(self):
        self._board = EMPTY_BOARD

    def add_board(self, board):
        self._board = board

    def solve(self, y=0, x=0):
        possible = True

        if self._board[y][x] == 0:
            horizontal_data = self._board[y]
            vertical_data = [self._board[i][x] for i in range(0, 9)]
            square_data = []

            _y = int(y / 3) * 3
            _x = int(x / 3) * 3
            for i in range(3):
                for j in range(3):
                    square_data.append(self._board[_y + i][_x + j])

            for num in range(1, 10):
                possible = True

                if possible and num in horizontal_data:
                    possible = False
                    continue

                if possible and num in vertical_data:
                    possible = False
                    continue

                if possible and num in square_data:
                    possible = False
                    continue

                self._board[y][x] = num

                possible = possible if y == 8 and x == 8 else self.solve(*self._get_new_y_and_x(y, x))

                if not possible:
                    self._board[y][x] = 0
                else:
                    return possible
            return possible

        else:
            return possible if y == 8 and x == 8 else self.solve(*self._get_new_y_and_x(y, x))

        return possible

    def _get_new_y_and_x(self, y, x):
        _y = y
        _x = x

        if x == 8:
            _y = y + 1
            _x = 0
        else:
            _x = x + 1

        return _y, _x

    def print_board(self):
        for i in range(len(self._board)):
            print(self._board[i])
