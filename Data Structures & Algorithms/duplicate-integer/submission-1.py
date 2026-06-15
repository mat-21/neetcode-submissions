class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        snums = set(nums)
        return len(nums) != len(snums)