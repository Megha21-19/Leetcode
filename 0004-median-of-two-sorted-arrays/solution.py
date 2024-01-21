class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged_array = sorted(nums1 + nums2)
        length = len(merged_array)

        if length % 2 == 1:
            # If the length is odd, return the middle element
            return float(merged_array[length // 2])
        else:
            # If the length is even, return the average of the two middle elements
            middle_left = length // 2 - 1
            middle_right = length // 2
            return (merged_array[middle_left] + merged_array[middle_right]) / 2.0

# Example usage

        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
