#https://leetcode.com/problems/isomorphic-strings/submissions/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        lhs=set(zip(s,t))
        rhs=set(zip(t,s))
        # print(lhs)
        # print(rhs)
        if len(lhs)==len(set(s)) and len(rhs)==len(set(t)):
            return True
        return False