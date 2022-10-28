"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by
deleting some (can be none) of the characters without disturbing the relative
positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""
class Solution(object):
    def isSubsequence(self, subsequence, some_string):
        """
        :type subsequence: str
        :type some_string: str
        :rtype: bool
        """
        subsequence_letters  = {}
        if len(subsequence) >  len(some_string):
            return False

        for letter in subsequence:
            if letter in subsequence_letters:
                subsequence_letters[letter] += 1
            else:
                subsequence_letters[letter] = 1

        for letter in some_string :
            if letter in subsequence_letters and subsequence_letters[letter] > 0:
                subsequence_letters[letter]-=1
            else:
                some_string = some_string.replace(letter, '', 1)

        return some_string == subsequence

test = Solution()
print(test.isSubsequence("axc", "ahbgdc"))
