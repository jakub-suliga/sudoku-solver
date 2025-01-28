class CheckerUtils:
    @staticmethod
    def is_valid(self, row, col, num, grid):
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