"""
the first of these solutions (mine) doesn't work
The second was basically solved using .set() which turns a list into a list of its individual parts
    say [3,4,5,4,6], set -> [2,4,5,6]
"""
def isntValidSudoku(board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        zipped = board[0]
        
        for row in board:
            tester = []
            for i in row:
                tester.append(i)
                if tester.count(i)>1 and i != ".":
                    return False
            if row != board[0]:
                zipped = zip(zipped, row)
        for column in zipped:
            cTester = []
            for i in column:
                cTester.append(i)
                if cTester.count(i)>1 and i != ".":
                    return False
            #print(cTester)
        #print(zipped)
        print(zipped[0])
        return True
        

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def isValidSudoku(self, board):
            return (self.is_row_valid(board) and
                    self.is_col_valid(board) and
                    self.is_square_valid(board))

        def is_row_valid(self, board):
            for row in board:
                if not self.is_unit_valid(row):
                    return False
            return True

        def is_col_valid(self, board):
            for col in zip(*board):
                if not self.is_unit_valid(col):
                    return False
            return True

        def is_square_valid(self, board):
            for i in (0, 3, 6):
                for j in (0, 3, 6):
                    square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                    if not self.is_unit_valid(square):
                        return False
            return True

        def is_unit_valid(self, unit):
            unit = [i for i in unit if i != '.']
            return len(set(unit)) == len(unit)



testBoard = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]


