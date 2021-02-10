from .Solution import Solution


def test_reverse():
    solution = Solution()

    assert solution.reverse(123) == 321
    assert solution.reverse(1234) == 4321
    assert solution.reverse(12345) == 54321

    assert solution.reverse(321) == 123
    assert solution.reverse(4321) == 1234
    assert solution.reverse(54321) == 12345

    assert solution.reverse(16382793) == 39728361


def test_reverse_zero_case():
    solution = Solution()

    assert solution.reverse(0) == 0


def test_reverse_negatives_returns_negative():
    solution = Solution()

    assert solution.reverse(-123) == -321
    assert solution.reverse(-1234) == -4321
    assert solution.reverse(-12345) == -54321

    assert solution.reverse(-321) == -123
    assert solution.reverse(-4321) == -1234
    assert solution.reverse(-54321) == -12345

    assert solution.reverse(-16382793) == -39728361


def test_reverse_overflow_returns_zero():
    solution = Solution()

    assert solution.reverse(solution.INT_32_MAX) == 0
