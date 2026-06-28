class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        l, r = 0, k - 1

        curr_max = max(nums[l:r+1])
        while r < len(nums):
            res.append(curr_max)

            l += 1
            r += 1

            if len(nums[l:r+1]) and nums[l-1] == curr_max:
                curr_max = max(nums[l:r+1])
            
            if r < len(nums) and nums[r] > curr_max:
                curr_max = nums[r]

        return res