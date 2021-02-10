from typing import List


class Solution:
    '''
    Solutions for Leetcode TwoSum variations
    '''

    def two_sum(self, nums: List[int], target: int) -> List[int]:
        '''
        Base TwoSum problem
        No assumptions about array ordering

        Difficulty: Easy
        '''

        numsLength = len(nums)

        results = [None] * 2
        currentIndex = 0
        lastIndex = numsLength - 1

        while results[0] is None and currentIndex <= lastIndex:
            for i in range(currentIndex + 1, numsLength):
                if(nums[i] + nums[currentIndex] == target):
                    results[0] = currentIndex
                    results[1] = i
                    break

            currentIndex += 1

        return results
