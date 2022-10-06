"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.

"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        copy_num = 0
        old_num = x
        if(x < 0):
            return False
        if(x == 0):
            return True
        while x > 0:
            copy_num = copy_num * 10 + x%10
            x = x//10
        return copy_num == old_num



print(Solution.isPalindrome(Solution, -123567653210))