"""
Given two strings ransomNote and magazine,
return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomNoteLetter_map = {}
        magazineLetter_map  = {}

        for letter in ransomNote:
            if letter in ransomNoteLetter_map:
                ransomNoteLetter_map[letter] +=1
            else:
                ransomNoteLetter_map[letter] = 1
        for letter in magazine:
            if letter in magazineLetter_map:
                magazineLetter_map[letter] += 1
            else:
                magazineLetter_map[letter] = 1
        #print(magazineLetter_map)
        #print(ransomNoteLetter_map)
        for letter in ransomNoteLetter_map:
            if letter in magazineLetter_map:
                magazineLetter_map[letter] -= ransomNoteLetter_map[letter]
                if(magazineLetter_map[letter] < 0):
                    return False
            else:
                return False

        #print(magazineLetter_map)
        #print(ransomNoteLetter_map)
        return True

test = Solution()
print(test.canConstruct("aa", "ab"))