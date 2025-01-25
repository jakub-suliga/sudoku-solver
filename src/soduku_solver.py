
class Soduko_Solver:
    def __init__(self, board, size=9):
        self.board = board
        self.size = size
    
    def solve(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    for num in range(1, 10):
                        if self.is_valid(i, j, num):
                            self.board[i][j] = num
                            if self.solve():
                                return True
                            self.board[i][j] = 0
                    return False
                
                
    def check_valid_in_row(self, row, num):
        for i in range(self.size):
            if self.board[row][i] == num:
                return False
    
    def check_valid_in_colum(self, col, num):
        for i in range(self.size):
            if self.board[i][col] == num:
                return False

    def check_valid_in_box(self, row, col, num):
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if self.board[i + start_row][j + start_col] == num:
                    return False
        return True
    
    def is_valid(self, row, col, num):
        return self.check_valid_in_row(row, num) and self.check_valid_in_colum(col, num) and self.check_valid_in_box(row, col, num)