from collections import Counter

"""
You are given two strings s and t.

String t is generated by random shuffling string s and then add one more letter at a random position.

Return the letter that was added to t.
"""
class Solution(object):
    def findTheDifference(self, starting_string, shuffled_string_with_added_letter):
        """
        :type starting_string: str
        :type shuffled_string_with_added_letter: str
        :rtype: str
        """
        starting_string = Counter(starting_string)
        print(starting_string)
        shuffled_string_with_added_letter = Counter(shuffled_string_with_added_letter)
        print(shuffled_string_with_added_letter)

        for letter, count in shuffled_string_with_added_letter.items():
            if starting_string.get(letter) is None:
                return letter
            if count > starting_string.get(letter):
                return letter


test = Solution()
print(test.findTheDifference("a", "aa"))