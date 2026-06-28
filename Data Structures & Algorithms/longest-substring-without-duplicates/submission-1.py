class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxsub = 0
        usub = set()
        for r in range(len(s)):
            print(l, r, s[l:r+1])
            if s[r] in usub:
                while s[r] in usub:
                    usub.remove(s[l])
                    l += 1
            usub.add(s[r])
            maxsub = max(maxsub, r - l + 1)
        return maxsub