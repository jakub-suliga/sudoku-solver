
class Soduko_Solver:
    def __init__(self, board):
        if not self.is_valid_board(board):
            return None
        self.board = board
        
    def is_valid_board(self, board):
        return True
    
    def solve(self):
        return self.board

if __name__ == "__main__":
    solver = Soduko_Solver([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    if solver is not None:
        solver.solve()