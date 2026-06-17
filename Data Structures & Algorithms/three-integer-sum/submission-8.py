class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for idx, i in enumerate(nums):
            if i > 0:
                break
            if idx > 0 and i == nums[idx - 1]:
                continue

            l, r = idx + 1, len(nums) - 1

            while l < r:

                three_sum = i + nums[l] + nums[r]

                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    result.append([i, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return result