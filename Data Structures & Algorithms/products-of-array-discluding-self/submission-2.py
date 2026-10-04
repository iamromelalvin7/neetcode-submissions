class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []

        output = []

        left, right = 1, 1
        for i in range(len(nums)):
            output.append(left)
            left *= nums[i]
            
        
        for j in range(len(nums)-1, -1, -1):
            output[j] *= right
            right *= nums[j]
            
            
        return output