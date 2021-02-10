from .Solution import Solution

MOCK_NUMS = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_two_sum():
    solution = Solution()

    assert solution.two_sum(MOCK_NUMS, 3) == [0, 1]
    assert solution.two_sum(MOCK_NUMS, 4) == [0, 2]
    assert solution.two_sum(MOCK_NUMS, 5) == [0, 3]
    assert solution.two_sum(MOCK_NUMS, 6) == [0, 4]
    assert solution.two_sum(MOCK_NUMS, 7) == [0, 5]
    assert solution.two_sum(MOCK_NUMS, 8) == [0, 6]
    assert solution.two_sum(MOCK_NUMS, 9) == [0, 7]
    assert solution.two_sum(MOCK_NUMS, 10) == [0, 8]

    assert solution.two_sum(MOCK_NUMS, 17) == [7, 8]
    assert solution.two_sum(MOCK_NUMS, 16) == [6, 8]
