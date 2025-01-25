import random
import soduku_solver

class SudokuGenerator:
    def __init__(self, size=9):
        self.size = size
        self.box_size = int(size ** 0.5)
        if self.box_size ** 2 != size:
            raise ValueError("Size must be a perfect square, e.g., 9 for a 9x9 Sudoku.")
    
    def generate_sudoku(self, level=40):
        """Generates a Sudoku puzzle with a given number of pre-filled cells (level)."""
        grid = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self._fill_grid(grid)
        self.print_grid(grid)
        print("\n")
        self._remove_cells(grid, self.size * self.size - level)
        return grid
    
    def _fill_grid(self, grid):
        """Fills the grid using backtracking to ensure a valid Sudoku."""
        for i in range(self.size):
            for j in range(self.size):
                if grid[i][j] == 0:
                    numbers = list(range(1, self.size + 1))
                    random.shuffle(numbers)
                    for num in numbers:
                        if self._is_valid(i, j, num, grid):
                            grid[i][j] = num
                            if self._fill_grid(grid):
                                return True
                            grid[i][j] = 0
                    return False
        return True
    
    def _remove_cells(self, grid, cells_to_remove):
        """Removes a specified number of cells to create the puzzle."""
        while cells_to_remove > 0:
            i = random.randint(0, self.size - 1)
            j = random.randint(0, self.size - 1)
            if grid[i][j] != 0:
                grid[i][j] = 0
                cells_to_remove -= 1
    
    def _is_valid(self, row, col, num, grid):
        """Checks if placing num at grid[row][col] is valid."""
        return (self._check_row(row, num, grid) and
                self._check_column(col, num, grid) and
                self._check_box(row, col, num, grid))
    
    def _check_row(self, row, num, grid):
        """Check if num is not in the given row."""
        return num not in grid[row]
    
    def _check_column(self, col, num, grid):
        """Check if num is not in the given column."""
        return all(grid[i][col] != num for i in range(self.size))
    
    def _check_box(self, row, col, num, grid):
        """Check if num is not in the corresponding box."""
        start_row = row - row % self.box_size
        start_col = col - col % self.box_size
        for i in range(self.box_size):
            for j in range(self.box_size):
                if grid[start_row + i][start_col + j] == num:
                    return False
        return True
    
    def print_grid(self, grid):
        """Prints the Sudoku grid in a readable format."""
        for i in range(self.size):
            if i % self.box_size == 0 and i != 0:
                print("-" * (self.size * 2 + self.box_size - 1))
            for j in range(self.size):
                if j % self.box_size == 0 and j != 0:
                    print("|", end=" ")
                print(grid[i][j] if grid[i][j] != 0 else ".", end=" ")
            print()

if __name__ == "__main__":
    generator = SudokuGenerator()
    sudoku = generator.generate_sudoku(level=30)  # 40 vorgegebene Zellen
    generator.print_grid(sudoku)
    print("\nSudoku-Rätsel generiert!")
    solver = soduku_solver.SudokuSolver(sudoku)
    if solver.solve():
        print("\nLösung:")
        solver.print_board()
    else:
        print("\nKeine Lösung gefunden.")
    
