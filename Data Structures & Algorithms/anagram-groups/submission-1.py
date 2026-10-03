class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        signature = [0] * 26

        i = 0
        j = 0
        while i < len(strs):
            if j == len(strs[i]):
                key = tuple(signature)
                
                if key in anagrams:
                    anagrams[key].append(strs[i])
                else:
                    anagrams[key] = [strs[i]]

                i += 1
                j = 0    
                signature = [0] * 26
                continue

            signature[ord(strs[i][j]) - ord('a')] += 1
            j += 1
    
        
        return list(anagrams.values())
                

