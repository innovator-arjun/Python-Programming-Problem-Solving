#https://leetcode.com/problems/intersection-of-two-arrays-ii/submissions/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        count = collections.Counter(nums1)
        res = []
        for i in nums2:
            if count[i] > 0:
                res.append(i)
                count[i] -= 1
        return res