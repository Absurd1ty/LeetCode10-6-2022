"""
You are playing the following Nim Game with your friend:

Initially, there is a heap of stones on the table.
You and your friend will alternate taking turns, and you go first.
On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
The one who removes the last stone is the winner.
Given n, the number of stones in the heap, return true if you can win
the game assuming both you and your friend play optimally, otherwise return false.
"""
"""
    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19  
    w w w l w w w l w w  w  l  w  w  w  l  w  w  w 
"""
class Solution(object):
    def canWinNim(self, number_of_stones):

        """
        :type number_of_stones: int
        :rtype: bool
        """
        if(number_of_stones % 4 == 0):
            return False
        else:
            return True
        """
        Made a big mistake in logic and overcomplicated a very simple problem. Its just multiples of 4....
        multiple_of_three = 0
        if(number_of_stones == 1 or number_of_stones == 2 or number_of_stones == 3):
            return True
        if(number_of_stones == 4):
            return False

        if (number_of_stones % 3 == 0):
            multiple_of_three = number_of_stones
        elif((number_of_stones+1) % 3 == 0):
            multiple_of_three = number_of_stones+1
        elif((number_of_stones-1) %3 == 0):
            multiple_of_three = number_of_stones-1

        return (multiple_of_three/3)%2==0
        """
test = Solution()
print(test.canWinNim(14))
