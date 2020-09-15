#https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = collections.Counter(s)
        t_count = collections.Counter(t)

        for i, val in t_count.items():
            if s_count[i] < val:
                return i