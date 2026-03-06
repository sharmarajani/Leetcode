class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1) , len(nums2)
        n = (n1+n2)//2
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        
        lo, hi = 0, n1
        left = (n1+n2+1)//2
        while lo <= hi:
            mid1 = (lo + hi) //2
            mid2 = left - mid1
            l1, l2, r1, r2 = float("-inf"), float("-inf"), float("inf"), float("inf")
            if mid1 < n1:
                r1=nums1[mid1]
            if mid2 < n2:
                r2= nums2[mid2]
            if mid1-1 >=0:
                l1 = nums1[mid1-1]
            if mid2-1>=0:
                l2 = nums2[mid2-1]
            if l1<=r2 and l2<=r1:
                total = n1+n2
                if total %2==1:
                    return float(max(l1, l2))
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1> r2:
                hi = mid1-1
            else:
                lo = mid1+1
        return 0
