## #8 String to Integer (atoi)
## Data: 2017.1.13

class Solution(object):
    def myAtoi(self, s):
        numset = [str(i) for i in range(10)]
        operatorset = ['+', '-']
        ret = s.strip()
        templist = []
        if len(s) <=0: return 0
        if s == '+' or s == '-': return 0
        if ret[0] not in numset and ret[0] not in operatorset:
            return 0
        if ret[0] in operatorset:
            templist.append(ret[0])
            ret = ret[1:]
        for ch in ret :
            if ch in numset: templist.append(ch)
            else: break
        ret = "".join(templist)
        if ret == '+' or ret == '-': return 0
        ret = int(ret)
        if ret > 2147483647: return 2147483647
        elif ret < -2147483648: return -2147483648
        else: return ret

temp = "  11w6"
print([str(i) for i in range(10)] + ['-', '+'])
print(Solution().myAtoi(temp))
print(temp)