"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:
"""
class Solution(object):
    def summaryRanges(nums):
        if not nums:
            return []
        start, prev, temp = nums[0], nums[0], str(nums[0])
        ranges_string = []
        nums.append(-1)
        for i in range(1, len(nums)):
            num = nums[i]
            if num - prev == 1:
                temp = f"{start}->{num}"
            else:
                ranges_string.append(temp)
                start = num
                temp = str(num)
            prev = num
        return ranges_string



test = Solution()
test = Solution.summaryRanges([0,2,3,4,6,8,9])
print(test)
