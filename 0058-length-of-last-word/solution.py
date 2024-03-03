class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.split()

        # Check if there are any words in the string
        if len(words) == 0:
            return 0

        # Return the length of the last word
        return len(words[-1])
        
