"""
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i],
we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum numbe
"""


class Solution:
    def findContentChildren(self, g, s) -> int:
        g.sort()
        s.sort()
        i = j = 0
        for cookie in s:
            if i >= len(g):
                return i
            if cookie >= g[i]:
                i += 1
        return i

test = Solution.findContentChildren(Solution, [1,2,3], [1,1])
print(test)