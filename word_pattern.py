"""
Here follow means a full match, such that there
is a bijection between a letter in pattern and a non-empty word in s.

"""

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s=s.split()
        if len(pattern) != len(s):
            return False
        matching_pattern_to_string = {}
        for word in s:
            if word not in matching_pattern_to_string.keys() and pattern[0] not in matching_pattern_to_string.values():
                matching_pattern_to_string[word]=pattern[0]
            else:
                if word not in matching_pattern_to_string.keys() or matching_pattern_to_string[word]!=pattern[0]:
                    return False
            #print(pattern)
            pattern=pattern[1:]
        return True

test = Solution()
print(test.wordPattern("abba", "dog cat cat dog"))