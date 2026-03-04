class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        res = []
        i , j = 0,0

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1

        while i < m:
            res.append(nums1[i])
            i += 1

        while j < n:
            res.append(nums2[j])
            j += 1

        if len(res) % 2 ==1:
            return res[len(res)//2]
            
            
        else:
            index = len(res)//2
            return (res[index] + res[index-1])/2
            
            


            