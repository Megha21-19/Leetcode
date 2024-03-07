import re

class Solution(object):
    def isPalindrome(self, s):
        # Use regular expression to filter alphanumeric characters and convert to lowercase
        cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        # Check if the cleaned string is equal to its reverse
        return cleaned_s == cleaned_s[::-1]
  


