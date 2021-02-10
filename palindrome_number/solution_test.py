from .Solution import Solution


def test_is_palindrome():
    solution = Solution()

    assert solution.isPalindrome(1001) == True
    assert solution.isPalindrome(10101) == True

    assert solution.isPalindrome(12345) == False
    assert solution.isPalindrome(101201) == False


def test_is_palindrome_negative_case():
    solution = Solution()

    assert solution.isPalindrome(-1001) == False
    assert solution.isPalindrome(-10101) == False

    assert solution.isPalindrome(-12345) == False
    assert solution.isPalindrome(-101201) == False
