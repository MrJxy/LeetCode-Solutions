## #38 Count and Say
## Date: 2017.02.26

class Solution(object):
    def countAndSay(self, n):
        if n == 1: return '1'
        prev = self.countAndSay(n - 1)
        l = [int(i) for i in [x for x in str(prev)]]
        count, num = 0, 0
        res = []
        for i in range(len(l)):
            if l[i] != num:
                if count != 0:
                    res.append(count)
                    res.append(num)
                count, num = 1, l[i]
            else:
                count += 1
        else:
            res.append(count)
            res.append(num)
        return "".join([str(i) for i in res])


print(Solution().countAndSay(6))
