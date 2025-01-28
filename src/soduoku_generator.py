import random
import copy

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
        print("Vollständig ausgefülltes Sudoku:")
        self.print_grid(grid)
        print("\nEntfernen von Zahlen zur Erstellung des Puzzles...\n")
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
        """Removes a specified number of cells to create the puzzle while ensuring uniqueness."""
        attempts = cells_to_remove
        while attempts > 0:
            i = random.randint(0, self.size - 1)
            j = random.randint(0, self.size - 1)
            if grid[i][j] != 0:
                backup = grid[i][j]
                grid[i][j] = 0

                grid_copy = copy.deepcopy(grid)
                if self._has_unique_solution(grid_copy):
                    attempts -= 1
                else:
                    grid[i][j] = backup     
    
    def _has_unique_solution(self, grid):
        """Checks if the given Sudoku grid has a unique solution."""
        self.solution_count = 0
        self._solve_sudoku(grid)
        return self.solution_count == 1
    
    def _solve_sudoku(self, grid):
        """Solves the Sudoku and counts the number of solutions."""
        for row in range(self.size):
            for col in range(self.size):
                if grid[row][col] == 0:
                    for num in range(1, self.size + 1):
                        if self._is_valid(row, col, num, grid):
                            grid[row][col] = num
                            self._solve_sudoku(grid)
                            grid[row][col] = 0
                    return
        self.solution_count += 1
        # Frühes Abbrechen, wenn mehr als eine Lösung gefunden wurde
        if self.solution_count > 1:
            return
    
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
    sudoku = generator.generate_sudoku(level=25)  # 30 vorgegebene Zellen
    print("Generiertes Sudoku-Rätsel mit eindeutiger Lösung:")
    generator.print_grid(sudoku)
    print("\nSudoku-Rätsel generiert!")
    try:
        import soduku_solver
        solver = soduku_solver.SudokuSolver(sudoku)
        if solver.solve():
            print("\nLösung:")
            solver.print_board()
        else:
            print("\nKeine Lösung gefunden.")
    except ImportError:
        print("\n'soduku_solver' Modul nicht gefunden. Lösung nicht angezeigt.")
