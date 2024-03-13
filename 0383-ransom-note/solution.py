class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        char_count = {}
        
        
        for char in magazine:
            char_count[char] = magazine.count(char)
    
        
        for char in ransomNote:
            if char not in char_count or char_count[char] == 0:
                return False
            char_count[char] -= 1
        
        return True

        
