#https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/submissions/
import numpy as np
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        su =sum(nums)
        res =[]
        for i in range(0 ,len(nums)):
            res.append(nums[i])
            su =su -nums[i]
            nums[i ] =0

            if sum(res ) >su:
                return res

