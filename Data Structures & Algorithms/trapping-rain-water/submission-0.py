class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lmost, rmost = height[l], height[r]
        result = 0
        while l < r:
            if lmost < rmost:
                l += 1
                lmost = max(lmost, height[l])
                result += lmost - height[l]
            else:
                r -= 1
                rmost = max(rmost, height[r])
                result += rmost - height[r]
        return result