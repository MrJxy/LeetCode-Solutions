## #17 Letter Combinations of a Phone Number
## Data:2017.1.14

class Solution(object):
    digit_dict = {1: '*', 2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno',
                  7: 'pqrs', 8: 'tuv', 9: 'wxyz', 0: ' '}
    def letterCombinations(self, digits):
        if digits == '0': return [' ']
        elif digits == '1': return ['*']
        elif digits == '2': return ['a', 'b', 'c']
        elif digits == '3': return ['d', 'e', 'f']
        elif digits == '4': return ['g', 'h', 'i']
        elif digits == '5': return ['j', 'k', 'l']
        elif digits == '6': return ['m', 'n', 'o']
        elif digits == '7': return ['p', 'q', 'r', 's']
        elif digits == '8': return ['t', 'u', 'v']
        elif digits == '9': return ['w', 'x', 'y', 'z']
        elif digits == '': return []
        digit = int(str(digits)[0])
        ret_digit = []
        left_digits = str(digits)[1:]
        sub_list = self.letterCombinations(left_digits)
        for ch in self.digit_dict[digit]:
            ret_digit += [ch + s for s in sub_list]
        return ret_digit

print(Solution().letterCombinations('12'))