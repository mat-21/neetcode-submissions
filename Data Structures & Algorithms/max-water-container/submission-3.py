class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_store = 0
        while l < r:
            print('heights[l], heights[r]', heights[l], heights[r])
            store = min(heights[l], heights[r]) * (r - l)
            print('store', store)
            if store > max_store:
                max_store = store
            
            lcand = heights[l]
            rcand = heights[r]

            if lcand > rcand:
                r -= 1
            elif lcand < rcand:
                l += 1
            else:
                l += 1
        
        return max_store