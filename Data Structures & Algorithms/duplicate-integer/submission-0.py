class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dup = set(nums)

        if len(nums) != len(nums_dup):
            return True
            
        return False