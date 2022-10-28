"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.
"""
class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """

        """
        Needlesly complicated with dict
        
        acceptable_primes = {2 ,3, 5}
        prime_counter = 2
        if(n<1):
            return False
        while(n>1):
            print(prime_counter)
            print(n)
            if(prime_counter != 4 and prime_counter not in acceptable_primes):
                return False
            if(n % prime_counter == 0):
                n = n/prime_counter
            else:
                prime_counter+=1
        return True
        """
        if n < 1 :
            return False
        elif n == 1 :
            return True
        while n % 2 == 0:
            n = n / 2
        while n % 3 == 0:
            n = n / 3
        while n % 5 == 0 :
            n = n / 5
        if n != 1 :
            return False
        return True



test = Solution()
print(test.isUgly(937351770))