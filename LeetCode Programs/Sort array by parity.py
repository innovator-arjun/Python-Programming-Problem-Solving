#https://leetcode.com/problems/sort-array-by-parity/submissions/

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        A.sort()
        res=[]
        for i in A:
            if i%2==0:
                res.insert(0,i)
            else:
                res.append(i)
        return res