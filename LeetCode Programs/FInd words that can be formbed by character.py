#https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

from collections import Counter
class Solution:
    def countCharacters(self, words:List[str], chars: str) -> int:
        chars_li =list(chars)
        char_count =Counter(chars)
        res =0
        for i in range(0 ,len(words)):
            flag =0
            for j in words[i]:
                # print(j)
                # print(words[i],words[i].count(j), chars_li.count(j))
                if words[i].count(j ) >chars_li.count(j):
                    flag =1
                    break
            if flag==0:
                res =res +len(words[i])

        return res