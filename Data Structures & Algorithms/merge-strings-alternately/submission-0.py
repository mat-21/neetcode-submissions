class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        one, two = 0, 0
        res = ''
        while one < len(word1) or two < len(word2):
            if one < len(word1):
                res += word1[one]
                one += 1
            
            if two < len(word2):
                res += word2[two]
                two += 1
        
        return res