from .Solution import Solution


def test_is_valid():
    solution = Solution()

    assert solution.isValid("()") == True
    assert solution.isValid("([])") == True
    assert solution.isValid("([{}])") == True
    assert solution.isValid("([]{}[])") == True
    assert solution.isValid("([]){}") == True
    assert solution.isValid("([])({})") == True

    assert solution.isValid("(") == False
    assert solution.isValid(")(") == False
    assert solution.isValid("(])") == False
    assert solution.isValid("([)]") == False
    assert solution.isValid("([{]}[])") == False
    assert solution.isValid("([}{}") == False
    assert solution.isValid("[()({})") == False
