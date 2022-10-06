"""
You are given a large integer represented as an integer array digits,
where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant
in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        """
        Solution 1
        number = 0
        for i in range(len(digits)):

            number += (10**(len(digits)-i-1) * digits[i])
        number += 1
        arr = []
        while(number >= 10):
            arr.append(number %10)
            number = number//10
        arr.append(number)
        arr.reverse()
        return arr
        
        """
        if(len(digits) == 1 and digits[0] == 9):
            return [1, 0]

        if(digits[-1] != 9):
            digits[-1] += 1
            return digits
        else:
            digits[-1] = 0
            digits[:-1] = self.plusOne(self, digits[:-1])
            return digits



test = Solution.plusOne(Solution, [9,9,9,9,9,9])
print(test)