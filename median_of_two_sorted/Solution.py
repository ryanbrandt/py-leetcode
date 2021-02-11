from typing import List
import math as m


class Solution:
    '''
    Simple problem to find the median of two sorted arrays

    Basic solution without any syntactic sugar. Merges the two arrays in n + m 
    and finds the median in constant time.

    Can also be done in log (n + m) if we divide and conquer

    Difficulty: Hard
    '''

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []

        nums1_len = len(nums1)
        nums2_len = len(nums2)

        j = 0

        for i in range(0, nums1_len):
            placed = False
            while j < nums2_len:
                if nums1[i] < nums2[j]:
                    merged.append(nums1[i])
                    placed = True
                    break

                merged.append(nums2[j])
                j += 1

            if not placed:
                merged.append(nums1[i])

        for k in range(j, nums2_len):
            merged.append(nums2[k])

        median_index = ((nums1_len + nums2_len) - 1) / 2
        median_lower = m.floor(median_index)
        median_upper = m.ceil(median_index)

        return (merged[median_lower] + merged[median_upper]) / 2
