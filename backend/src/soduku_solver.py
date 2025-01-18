
class Soduko_Solver:
    def __init__(self, board, size=9):
        self.board = board
        self.size = size
    
    def solve(self):
        for i in range(self.size):
            for j in range(self.size):
                return NotImplementedError
                

if __name__ == "__main__":
    solver = Soduko_Solver([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    if solver is not None:
        solver.solve()