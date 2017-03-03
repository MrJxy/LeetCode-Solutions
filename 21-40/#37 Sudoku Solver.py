## #37 Sudoku Solver
## Date: 2017.1.19




## Not accepted
## Right answers but different to given answers
## TBD

import numpy as np

class Solution(object):
    def isValidPart(self, mat):
        buf = set()
        for keys in mat:
            for key in keys:
                if key in buf and key != '.':
                    return False
                else:
                    buf.add(key)
        return True

    def isValidSudoku(self, ch_mat):
        for i in range(9):
            line = ch_mat[i:i+1, 0:9]
            column = ch_mat[0:9, i:i+1]
            if not (self.isValidPart(line) and self.isValidPart(column)):
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                part = ch_mat[i:i+3, j:j+3]
                if not self.isValidPart(part):
                    return False
        return True

    def solve(self, ch_mat, x):
        # ch_list = []
        # for l in board:
        #     for ch in l:
        #         ch_list.append(ch)
        # ch_mat = np.array(ch_list).reshape((9, 9))
        if not '.' in ch_mat:
            return 0
        for i in range(x, 9):
            for j in range(0, 9):
                if ch_mat[i][j] == '.':
                    for num in range(10):
                        ch_mat[i][j] = str(num)
                        if self.isValidSudoku(ch_mat):
                            print(i, j)
                            recur = self.solve(ch_mat, i)
                            if recur == 0: return recur
                    else:
                        ch_mat[i][j] = '.'
                        return -1


    def solveSudoku(self, board):
        ch_list = []
        for l in board:
            for ch in l:
                ch_list.append(ch)
        ch_mat = np.array(ch_list).reshape((9,9))
        self.solve(ch_mat, 0)
        for i in range(9):
            board[i] = ''.join(ch_mat[i])

a = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
Solution().solveSudoku(a)
print(a)
