class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ''
        for s in strs:
            ls = len(s)
            result += f'{ls}#{s}'
        print('encode result', result)
        return result

    def decode(self, s: str) -> List[str]:
        print('decode s', s)
        ptr = 0
        ls = ''
        strs = []
        while ptr < len(s):
            if s[ptr] == '#':
                lc = int(ls)
                strs.append(s[ptr+1:ptr+1+lc])
                ptr += lc + 1
                ls = ''
                continue
            ls += s[ptr]
            ptr += 1
            print(ls)
        return strs


