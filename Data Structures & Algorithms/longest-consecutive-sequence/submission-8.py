class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        snums = set(nums)
        max_streak = 0
        for num in snums:
            streaking = True
            curr_streak = 1
            curr = num
            while streaking:
                if curr + 1 in snums:
                    curr_streak += 1
                    curr += 1
                    print(num, curr)
                else:
                    streaking = False
                
            if curr_streak > max_streak:
                max_streak = curr_streak

        return max_streak