import math as m


class Solution:
    '''
    Solutions for leetcode Palindrome Number variations
    '''

    def checkChar(self, strX, i, j) -> bool:
        if(i >= j):
            return True

        if(strX[i] == strX[j]):
            return self.checkChar(strX, i + 1, j - 1)

        return False

    def isPalindrome(self, x: int) -> bool:
        '''
        Basic Palindrome Number problem

        We can also use an approach similiar to the reverse_integer problem,
        but this is a decently efficient and readable solution.

        Difficulty: Easy
        '''

        if x < 0:
            return False

        strX = str(x)

        return self.checkChar(strX, 0, len(strX) - 1)
