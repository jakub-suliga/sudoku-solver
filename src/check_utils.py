class CheckerUtils:
    @staticmethod
    def is_valid(row, col, num, grid, size=9, box_size=3):
        """Checks if placing num at grid[row][col] is valid."""
        return (CheckerUtils._check_row(row, num, grid) and
                CheckerUtils._check_column(col, num, grid, size) and
                CheckerUtils._check_box(row, col, num, grid, box_size))
     
    @staticmethod
    def _check_row(row, num, grid):
        """Check if num is not in the given row."""
        return num not in grid[row]
    
    @staticmethod
    def _check_column(col, num, grid, size):
        """Check if num is not in the given column."""
        return all(grid[i][col] != num for i in range(size))
    
    @staticmethod
    def _check_box(row, col, num, grid, box_size):
        """Check if num is not in the corresponding box."""
        start_row = row - row % box_size
        start_col = col - col % box_size
        for i in range(box_size):
            for j in range(box_size):
                if grid[start_row + i][start_col + j] == num:
                    return False
        return True
