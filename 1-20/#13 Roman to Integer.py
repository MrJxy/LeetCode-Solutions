## #13 Roman to Integer
## Data: 2017.1.13

class Solution(object):
    def romanToInt(self, s):
        rev = s[::-1]
        roman_dict = dict(I = 1, V = 5, X = 10, L = 50,
                          C = 100, D = 500, M = 1000)

        ret = 0
        prev = 0
        for ch in rev:
            if roman_dict[ch] >= prev:
                ret += roman_dict[ch]
            else:
                ret -= roman_dict[ch]
            prev = roman_dict[ch]
        return ret

print(Solution().romanToInt('MCMXC'))