"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string " ".
"""

class Solution:
    def longestCommmonPrefix(self, strs: [str]) -> str:
        answer = " "
        if not strs:
            return " "
        elif (len(strs) == 1):
            return strs[0]
        else:
            strs.sort
            for i in range(len(strs[0])):
                if strs[0][i] == strs[-1][i]:
                    answer += strs[0][i]
                else:
                    break
        return answer

test =Solution.longestCommmonPrefix(Solution, ["flower", "flow", "flight"])
print(test)