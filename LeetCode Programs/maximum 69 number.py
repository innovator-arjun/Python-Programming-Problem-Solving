#https://leetcode.com/problems/maximum-69-number/submissions/
class Solution:
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace('6' ,'9' ,1))
#         li=list(str(num))
#         res=''
#         flag=0
#         for i in li:
#             if i=='6' and flag==0:
#                 res+='9'
#                 flag=1
#             else:
#                 res+=i

#         return res