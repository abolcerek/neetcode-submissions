class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0 #counter variable that counts the number of 1's
        while n: #while there are numbers in n
            res += n % 2 #res is incrementally equal to modulo 2 of n since the modulo value while determine if its a 1 or not
            n = n >> 1 #we move the bits to the right so we can modulo the next bit
        return res #we return res which has counted all the ones