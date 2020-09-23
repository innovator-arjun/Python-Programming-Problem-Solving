#https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/submissions/

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        col = collections.Counter(arr)
        for i, val in col.items():
            if val / len(arr) > 0.25:
                return i
