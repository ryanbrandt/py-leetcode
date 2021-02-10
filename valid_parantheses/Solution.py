class Solution:
    '''
    Solutions for Leetcode Valid Parantheses variations
    '''

    CLOSING_PARAN = ")"
    CLOSING_CURLY = "}"
    CLOSING_BRACKET = "]"

    OPEN_PARAN = "("
    OPEN_CURLY = "{"
    OPEN_BRACKET = "["

    def isValid(self, s: str) -> bool:
        '''
        Base is Valid Parantheses problem

        Pretty simple problem, solvable with a stack.
        Push in stack if a opening paran.
        Validate that the top of the stack is the associated
        opening paran if a closing paran.

        Difficulty: Easy
        '''

        openers = [Solution.OPEN_BRACKET,
                   Solution.OPEN_CURLY, Solution.OPEN_PARAN]
        closers = [Solution.CLOSING_BRACKET,
                   Solution.CLOSING_CURLY, Solution.CLOSING_PARAN]

        sLen = len(s)
        stack = []

        for i in range(0, sLen):
            paran = s[i]

            if paran in openers:
                stack.append(paran)
            else:
                if len(stack) < 1:
                    return False
                else:
                    first = stack.pop()
                    closesProperly = True

                    if paran == Solution.CLOSING_PARAN:
                        closesProperly = first == Solution.OPEN_PARAN

                    if paran == Solution.CLOSING_BRACKET:
                        closesProperly = first == Solution.OPEN_BRACKET

                    if paran == Solution.CLOSING_CURLY:
                        closesProperly = first == Solution.OPEN_CURLY

                    if not closesProperly:
                        return False

        return len(stack) == 0
