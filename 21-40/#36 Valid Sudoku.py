## #36 Valid Sudoku
## Date: 2017.1.19
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

    def isValidSudoku(self, board):
        ch_list = []
        for l in board:
            for ch in l:
                ch_list.append(ch)
        ch_mat = np.array(ch_list).reshape((9,9))


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


print(Solution().isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]))