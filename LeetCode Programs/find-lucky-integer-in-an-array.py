#https://leetcode.com/problems/find-lucky-integer-in-an-array/submissions/
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        co =collections.Counter(arr)
        max_val =sorted(list(co.values()) ,reverse=True)
        for num in max_val:
            if num in arr:
                if arr.count(num )==num:
                    return num
        return -1

#         print(max_val)
#         for i,val in co.items():
#             if i==val and i==max_val:
#                 return i

#         return -1