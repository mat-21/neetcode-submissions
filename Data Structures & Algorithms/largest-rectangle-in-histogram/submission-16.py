class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for idx, h in enumerate(heights):
            print('1', idx, h)

            left, right = heights[:idx], heights[idx:]
            left.reverse()
            print('l', len(left), 'r', len(right))

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
            print('c', len(candidates))
            area = h * len(candidates)
            print('2', area, max_area)
            if area > max_area:
                max_area = area
                    
        return max_area