class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for idx, temp in enumerate(temperatures):
            warmer_days = 0
            found = False
            for temp2 in temperatures[idx+1:]:
                warmer_days += 1
                if temp2 > temp:
                    found = True
                    break
            if found:
                result.append(warmer_days)
            else:
                result.append(0)
        return result