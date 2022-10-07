"""
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        if n==0:
            return False
        if n==3 or n==1:
            return True

        multiply = 3
        while(multiply < n):
            multiply = multiply * 3
        """"if multiply > n: 
            return False"""
        if multiply == n:
            return True
        else:
            return False

test = Solution.isPowerOfThree(Solution, 82)
print(test)