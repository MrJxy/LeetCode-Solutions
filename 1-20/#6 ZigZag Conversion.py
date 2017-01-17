## #6 ZigZag Conversasion
## Data: 2017.1.13

class Solution(object):
    def convert(self, s, numRows):
        if numRows <= 1: return s
        arr = [[] for i in range(numRows)]
        index, zigzag = 0, True
        for ch in s:
            arr[index].append(ch)
            index = index + 1 if zigzag else index - 1
            if index==numRows-1 : zigzag = False
            if index==0: zigzag = True
        ret = ""
        for substr in arr:
            ret += "".join(substr)
        return ret

print(Solution().convert("aaa", 1))
