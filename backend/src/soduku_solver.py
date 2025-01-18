
class Soduko_Solver:
    def __init__(self, board):
        self.board = board
    
    def solve(self):
        return self.board

if __name__ == "__main__":
    solver = Soduko_Solver([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    if solver is not None:
        solver.solve()