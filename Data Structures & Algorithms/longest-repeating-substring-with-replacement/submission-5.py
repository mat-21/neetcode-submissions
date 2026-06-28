class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_set = set(s)
        maxsub = 0
        for c in char_set:
            l = count = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                
                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    
                    l += 1
                
                maxsub = max(maxsub, (r-l+1))
        return maxsub