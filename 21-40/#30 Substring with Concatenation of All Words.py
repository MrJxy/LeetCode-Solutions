## #30 Substring with Concatenation of All Words
## Date: 2017.1.15


## To Be Done
## Not Perfect: note line 15


class Solution(object):
    def findSubstring(self, s, words):
        word_num = len(words)
        if word_num == 0: return []
        word_len = len(words[0])
        if word_len == 0: return [i for i in range(len(s) + 1)]
        if word_len * word_num > len(s): return []
        indices_list = []
        hash_map = dict()
        for w in words:
            if w in hash_map:
                hash_map[w] += 1
            else:
                hash_map[w] = 1

        # words_set = set(words)
        for i in range(len(s)):
            if i+word_len > len(s): break
            if s[i:i+word_len] in hash_map:
                temp = dict(hash_map)
                for j in range(i, i + word_len * word_num, word_len):
                    slicestr = s[j:j+word_len]
                    if slicestr not in temp or temp[slicestr] == 0:
                        break
                    if slicestr in temp:
                        temp[slicestr] -= 1

                else: indices_list.append(i)
        return indices_list

print(Solution().findSubstring("barfoothefoobarman", ["foo","bar"]))
