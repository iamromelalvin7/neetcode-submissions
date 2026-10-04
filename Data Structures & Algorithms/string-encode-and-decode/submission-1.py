class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        sizes, enc = [] , []

        for string in strs:
            sizes.append(len(string))
        for sz in sizes:
            enc.append(str(sz))
            enc.append(',')
        enc.append('#')
        enc.extend(strs)
        return ''.join(enc)

        
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, dec, i = [], [], 0
        while s[i] != '#':
            j = i
            while s[j] != ',':
                j += 1
            sizes.append(int(s[i:j]))
            i = j + 1
        i += 1

        for sz in sizes:
            dec.append(s[i:i + sz])
            i += sz
        return dec
