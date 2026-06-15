class Solution:
    def isValid(self, s: str) -> bool:
        if not s or len(s) == 1:
            return False
        close_values_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        opening_values = set(['(', '[', '{'])
        ordered_values = []
        for c in s:
            if c in close_values_map:
                try:
                    prev = ordered_values.pop()
                except:
                    return False

                if prev != close_values_map[c]:
                    return False
            else:
                ordered_values.append(c)

        return not bool(len(ordered_values))