#https://leetcode.com/problems/matrix-diagonal-sum/submissions/
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res =0
        length1 =len(mat[0])
        temp =length1
        while(length1!=0):
            res=res+ mat[length1 -1][length1 -1 ]+ mat[temp -length1][length1 -1]

            length1 =length1 -1
        # temp=length1
        # while(length1!=0):
        #     res=res+ mat[temp-length1][length1-1]
        #     length1=length1-1
        if temp % 2==0:
            return res
        else:
            return res -mat[int(temp /2)][int(temp /2)]


