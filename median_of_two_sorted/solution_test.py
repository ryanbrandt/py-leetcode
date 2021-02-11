from .Solution import Solution


def test_find_median():
    solution = Solution()

    assert solution.findMedianSortedArrays([1], [1, 2]) == 1
    assert solution.findMedianSortedArrays([], [1]) == 1
    assert solution.findMedianSortedArrays([1, 3, 8], [9, 12]) == 8
    assert solution.findMedianSortedArrays([1, 3], [9, 12]) == 6
    assert solution.findMedianSortedArrays([1, 3, 22, 48, 55], [9, 12]) == 12
    assert solution.findMedianSortedArrays(
        [1, 3, 22, 48, 55], [9, 10, 13]) == 11.5
