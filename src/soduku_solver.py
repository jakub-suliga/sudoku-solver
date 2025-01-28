from check_utils import CheckerUtils


class SudokuSolver:
    def __init__(self, board, size=9):
        self.board = board
        self.size = size
        self.box_size = int(size ** 0.5)
        if self.box_size ** 2 != size:
            raise ValueError("Size must be a perfect square, e.g., 9 for a 9x9 Sudoku.")

    def solve(self):
        """Löst das Sudoku-Raster mittels Backtracking."""
        empty = self._find_empty()
        if not empty:
            return True  # Sudoku ist gelöst
        row, col = empty

        for num in range(1, self.size + 1):
            if CheckerUtils.is_valid(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = 0  # Rückgängigmachen

        return False  # Keine Lösung gefunden

    def _find_empty(self):
        """Findet die nächste leere Zelle im Raster. Gibt (row, col) zurück oder None."""
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    def print_board(self):
        """Gibt das Sudoku-Raster in einem lesbaren Format aus."""
        for i in range(self.size):
            if i % self.box_size == 0 and i != 0:
                print("-" * (self.size * 2 + self.box_size - 1))
            for j in range(self.size):
                if j % self.box_size == 0 and j != 0:
                    print("|", end=" ")
                print(self.board[i][j] if self.board[i][j] != 0 else ".", end=" ")
            print()
