"""
Given an array of integers nums and an
integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would
have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

In essence int1+int2=target
target - int1 = int2
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """


        """
        This solutiuon passes all tests but is too long, looking into it hashtable was the best solution
        
        number_index = 0
        for index, number in enumerate(nums):
            remainder = target - number
            number_index = index
            #print(index)
            for index, number in enumerate(nums):
                #print(number)
                #print(index)
                if number == remainder and number_index != index:
                    return (number_index, index)
        """

        """
        Second Solution with hashtable where we store index of the number
        """
        hashtable = {}
        for index, number in enumerate(nums):
            remainder = target - number
            if remainder in hashtable:
                return[index, hashtable[remainder]]
            else:
                hashtable[number] = index


test = Solution.twoSum(Solution, [3,2,4], 6)
print(test)