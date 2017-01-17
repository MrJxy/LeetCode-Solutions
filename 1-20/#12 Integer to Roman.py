## #12 Integer to Roman
## Data: 2017.1.13

class Solution(object):
    def intToRoman(self, num):
        q, m = divmod(num, 1000)
        thousands, hundreds, tens, digits = [], [], [], []
        for i in range(q):
            thousands.append('M')
        q, m = divmod(m, 100)
        if q >= 9: hundreds.append('CM')        ## 9
        elif q >= 5:                            ## 5, 6, 7, 8
            temp = q - 5
            hundreds.append('D')
            for i in range(temp): hundreds.append('C')
        elif q >= 4:                            ## 4
            hundreds.append('CD')
        else:                                   ## 1, 2, 3
            for i in range(q): hundreds.append('C')
        q, m = divmod(m, 10)
        if q >= 9: tens.append('XC')
        elif q >= 5:
            temp = q - 5
            tens.append('L')
            for i in range(temp): tens.append('X')
        elif q >= 4:
            tens.append('XL')
        else :
            for i in range(q): tens.append('X')
        if m >= 9: digits.append('IX')
        elif m >= 5:
            temp = m - 5
            digits.append('V')
            for i in range(temp): digits.append('I')
        elif m >= 4:
            digits.append('IV')
        else:
            for i in range(m): digits.append('I')
        return ''.join(thousands) + ''.join(hundreds) + ''.join(tens) + ''.join(digits)

print(Solution().intToRoman(1234))

