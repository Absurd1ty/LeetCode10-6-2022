"""
You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores,
where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.
"""
class Solution:
    def findRelativeRanks(self, score):

        score_copy = score.copy()
        #print(score_copy)
        score_copy.sort(reverse=True)
        #print(score_copy)
        relative_ranks = []
        for i in score:
            if score_copy.index(i) == 0:
                relative_ranks.append("Gold Medal")
            elif score_copy.index(i) == 1:
                relative_ranks.append("Silver Medal")
            elif score_copy.index(i) == 2:
                relative_ranks.append("Bronze Medal")
            else:
                relative_ranks.append(str(score_copy.index(i)+1))
        return relative_ranks


test = Solution()
print(test.findRelativeRanks([10,3,8,9,4]))
