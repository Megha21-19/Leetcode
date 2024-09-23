class Solution:
    def twoSum(self, nums, target):
        # Iterate through each element
        for i in range(len(nums)):
            # For each element, check all subsequent elements
            for j in range(i + 1, len(nums)):
                # If the sum of two numbers equals the target, return their indices
                if nums[i] + nums[j] == target:
                    return [i, j]


        
