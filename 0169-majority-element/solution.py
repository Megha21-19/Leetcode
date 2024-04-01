class Solution(object):
    def majorityElement(self, nums):
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        max_count = max(counts.values())
        majority_element = max(counts, key=counts.get)
        
        return majority_element
        
