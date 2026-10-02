class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for st in strs:
            _sorted = "".join(sorted(st))
            if _sorted in anagrams:
                anagrams[_sorted].append(st)
            else:
                anagrams[_sorted] = [st]
        
        return list(anagrams.values())
                

