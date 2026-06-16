class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for idx, h in enumerate(heights):

            left, right = heights[:idx], heights[idx:]
            left.reverse()

            candidates = []
            for candidate in left:
                if candidate >= h:
                    candidates.append(candidate)
                else:
                    break
            for candidate in right:
                if candidate >= h:
                    candidates.append(candidate)
                else:
                    break
            area = h * len(candidates)
            if area > max_area:
                max_area = area
                    
        return max_area