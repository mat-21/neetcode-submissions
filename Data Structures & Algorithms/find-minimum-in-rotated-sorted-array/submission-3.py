class Solution:
    def findMin(self, nums: List[int]) -> int:
        # no rotation
        if nums[-1] > nums[0]:
            return nums[0]
        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r - l) // 2)

            if r - l == 1:
                if nums[r] > nums[l]:
                    return nums[l]
                return nums[r]

            if nums[m] > nums[r]:
                l = m
            else:
                r = m