class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        cache = {}
        for idx, num in enumerate(numbers):
            idx = idx + 1
            if num in cache:
                return [cache[num], idx]

            
            res = target - num
            cache[res] = idx

            
        return []