import random


class sodoku_generaotr:
    def __init__(self):
        pass
    
    def generated_sodoku(self, size, level):
        result = [[0 for i in range(size)] for j in range(size)]
        
        for i in range(size):
            for j in range(size):
                rnd = random.randint(1,level)
                if rnd == 1:
                    random_num = random.randint(1, 9)
                    while not self.is_valid(i, j, random_num, result):
                        random_num = random.randint(1, 9)
                    result[i][j] = random_num
        return result
    
    def check_valid_in_row(self, row, num, result):
        for i in range(len(result)):
            if result[row][i] == num:
                return False
        return True
            
    def check_valid_in_colum(self, col, num, result):
        for i in range(len(result)):
            if result[i][col] == num:
                return False
        return True
            
    def check_valid_in_box(self, row, col, num, result):
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if result[i + start_row][j + start_col] == num:
                    return False
        return True

    def is_valid(self, row, col, num, result):
        return True
    
    
if __name__ == "__main__":
    sodoku = sodoku_generaotr()
    print(sodoku.generated_sodoku(9, 1))