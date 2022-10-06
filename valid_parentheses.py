"""
Given a string s containing jus the chracters ( ) { } [ ] determinet if the input string is valid

An input string is valid. 1. Open brackets must be closed by the same tpye of brackets.
2. Open brackets must be closed in the correct order.
3. Every close brcaket has a corresponding open brcaket of the same type.
"""

class Solution():
    def isValid(self, s: str) -> bool:
        """

        Bad time complexity because of replace. Will do aother solution.

        while (len(s) > 0):
            l = len(s)
            s = s.replace('( )', '').replace('{ }', '').replace('[ ]', '')
            if l == len(s): return False
        return True
        """


test = Solution.isValid(Solution, " ( ) [ ] { } ")
print (test)
