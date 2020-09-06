#https://leetcode.com/problems/reverse-only-letters/solution/

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        rev=str(S[::-1])
        non_alpha=''.join([i for i in rev if i.isalpha()])
        res=''
        length=0
        for i in S:
            if i.isalpha():
                res=res+non_alpha[length]
                length+=1
            else:
                res=res+i
        return res