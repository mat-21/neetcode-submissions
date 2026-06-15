import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for idx, n in enumerate(nums):
            left = []
            right = []

            if idx != 0:
                left = nums[:idx]

            if idx + 1 != len(nums):
                right = nums[idx+1:]

            candidates = left + right
            result.append(math.prod(candidates))


        return result