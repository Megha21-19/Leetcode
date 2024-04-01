class Solution(object):
    def countBits(self, n):
        def count_ones_in_binary(binary):
            return binary.count('1')

        binary_ones_counts = []
        for i in range(n+1):
            binary = bin(i)[2:]  
            ones_count = count_ones_in_binary(binary)
            binary_ones_counts.append(ones_count)
        return binary_ones_counts
        
