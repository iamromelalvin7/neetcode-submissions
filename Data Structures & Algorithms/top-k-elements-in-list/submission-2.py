class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        output = []
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1

        freq = sorted(list(set(seen.values())), reverse=True)

        while freq and len(output) < k:
            f = freq.pop(0)
            for key, value in seen.items():
                if value == f:
                    output.append(key)

        return output

