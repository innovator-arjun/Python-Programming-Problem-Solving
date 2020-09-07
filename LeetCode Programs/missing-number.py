#https://leetcode.com/problems/missing-number/submissions/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # nums=[0]
        m = len(nums)
        form = (m * (m + 1)) / 2
        su = sum(nums)
        return int(form - su)
