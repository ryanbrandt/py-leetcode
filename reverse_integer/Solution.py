import math as m


class Solution:
    '''
    Solutions for leetcode Reverse Integer variations
    '''

    INT_32_MAX = 2147483647
    DECIMAL_BASE = 10

    def reverse(self, x: int) -> int:
        '''
        Base Reverse Integer problem
        Reverse integer, while assuming an environment bound of +/- INT_32_MAX

        Difficulty: Easy
        '''

        runningX = abs(x)
        result = 0

        if runningX > 0:
            n = m.floor(m.log(runningX, 10))
            i = n

            while i >= 0:
                result += m.floor((runningX % Solution.DECIMAL_BASE) *
                                  m.pow(Solution.DECIMAL_BASE, i))
                runningX = m.floor(runningX / Solution.DECIMAL_BASE)

                if(result > Solution.INT_32_MAX):
                    result = 0
                    break

                i -= 1

            if(x < 0):
                result = result * -1

        return result
