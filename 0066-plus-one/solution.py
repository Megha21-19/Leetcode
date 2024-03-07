class Solution(object):
    def plusOne(self, digits):
        num = int(''.join(map(str, digits)))


        num += 1

        result_digits = [int(digit) for digit in str(num)]

        return result_digits


        
        
