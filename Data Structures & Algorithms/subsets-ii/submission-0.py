class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        combos = set()

        def backtrack(i, combo):
            if i == len(nums):
                combos.add(tuple(combo))
                return
            
            combo.append(nums[i])
            backtrack(i+1, combo)
            combo.pop()
            backtrack(i+1, combo)

        backtrack(0, [])
        return [list(combo) for combo in combos]