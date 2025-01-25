
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
                
                
    def check_valid_in_row():
        return NotImplementedError
    
    def check_valid_in_colum():
        return NotImplementedError

    def check_valid_in_box():
        return NotImplementedError
    
    def is_valid(self, row, col, num):
        return self.check_valid_in_row(row, num) and self.check_valid_in_colum(col, num) and self.check_valid_in_box(row, col, num)