#https://leetcode.com/problems/occurrences-after-bigram/submissions/

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res = []
        li = text.split(" ")

        for i in range(0, len(li) - 2):
            if li[i] == first and li[i + 1] == second:
                res.append(li[i + 2])
        return res