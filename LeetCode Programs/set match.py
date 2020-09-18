#https://leetcode.com/problems/set-mismatch/submissions/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        li = set(list(range(1, len(nums) + 1)))
        nums_set = set(nums)
        res = list(li ^ nums_set)
        # print(type(res))
        nums_count = collections.Counter(nums)
        for i, v in nums_count.items():
            if v == 2:
                return list([i, res[0]])
