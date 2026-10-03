class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        output = []
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1

        freq = sorted(seen.keys(),key=lambda num: seen[num], reverse=True)
        
        return freq[:k]

