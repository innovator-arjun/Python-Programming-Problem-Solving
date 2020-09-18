
#https://leetcode.com/problems/rotate-string/submissions/

class Solution:
    def rotateString(self, A: str, B: str) -> bool:

        temp=''
        if A==B:
            return True
        for i in range(1,len(A)):
            shift=A[0:i]
            temp=A[i:len(A)] +shift
            if temp==B:
                # print(temp)
                return True
            # print(temp)
        return False