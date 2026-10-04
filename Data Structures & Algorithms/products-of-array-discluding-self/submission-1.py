class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []

        output = []

        left, right = 1, 1
        for i in range(len(nums)):
            if i == 0:
                output.append(left)
                continue
            
            left *= nums[i-1]
            output.append(left)
        
        for j in range(len(nums)-2, -1, -1):
            right *= nums[j+1]
            output[j] *= right
            
        return output