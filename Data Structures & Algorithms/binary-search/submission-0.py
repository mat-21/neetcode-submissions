class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0 , len(nums) - 1

        while l <= r:
            mid_idx = l + ((r - l) // 2)
            mid_val = nums[mid_idx]

            if mid_val == target:
                return mid_idx
            elif mid_val > target:
                r = mid_idx - 1
            else:
                l = mid_idx + 1
        return -1