class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        index_dict = {}
        
        for i in range(len(nums)):
            if nums[i] in index_dict:
                diff = i - index_dict[nums[i]]
                if diff <= k:
                    return True
            
            index_dict[nums[i]] = i
        
        return False

