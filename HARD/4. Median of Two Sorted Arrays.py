class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # variables initialize 
        N1, N2 = len(nums1), len(nums2)
        # set right and left boundary
        lo, hi = 0, 2 * N2
        # make sure the nums1 is the larger one
        if N2 > N1:
            return self.findMedianSortedArrays(nums2,nums1)
        # when left boundary not larger than right, keep looping
        while (lo <= hi):
            # position the cut point at nums2
            mid2 = floor((lo + hi) / 2)
            # position the cut point at nums1 regarding to the cut of nums2
            mid1 = N1 + (N2 - mid2)
            # get the number near the cut point, noted that if cut point is at 0 or N2 means cut at boundary and make it stop so define it as inf 
            L1 = -inf if (mid1 == 0) else nums1[floor((mid1 - 1) / 2)]
            R1 = inf if mid1 == 2*N1 else nums1[floor(mid1 / 2)]
            L2 = -inf if mid2 == 0 else nums2[floor((mid2 - 1) / 2)]
            R2 = inf if mid2 == 2*N2 else nums2[floor(mid2 / 2)]
            
            # if L1 bigger than R2, the cut point of nums2 need move right
            if R2 < L1:
                lo = mid2+1
            # on the contrary
            elif R1 < L2:
                hi = mid2-1
            # if R1 > L2 and R2 > L1 means it find the median cut point
            else:
                return (min(R1, R2) + max(L1, L2)) / 2
