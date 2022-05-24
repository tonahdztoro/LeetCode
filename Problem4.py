class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        sort = sorted(merged)
        median = 0
        if len(sort)%2 != 0:
            median = sort[int(len(sort)/2)]
        else:
            median = ( sort[int(len(sort)/2)] + sort[int(len(sort)/2 - 1)] )/2
        
        return median
