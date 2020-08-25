#https://leetcode.com/problems/minimum-absolute-difference/submissions/

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_abs = 1000000
    #Find the min_abs value
        for i in range(0, len(arr) - 1):
            # print(arr[i+1],arr[i])
            if abs(arr[i + 1] - arr[i]) < min_abs:
                min_abs = abs(arr[i + 1] - arr[i])
        # print(min_abs)
        # print('/n')
    # Find the pairs that has min_abs value
        final = []
        for i in range(0, len(arr) - 1):
            if abs(arr[i + 1] - arr[i]) == min_abs:
                # print(arr[i+1],arr[i])
                res = [arr[i], arr[i + 1]]
                final.append(res)
        return final