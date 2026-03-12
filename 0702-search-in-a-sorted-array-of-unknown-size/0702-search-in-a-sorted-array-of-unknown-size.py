# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        l, h = 0,1
        while reader.get(h) < target:
            l= h
            h = h*2
        while l <= h :
            mid = (l+h)//2
            if reader.get(mid) == target:
                return mid
            if reader.get(mid) > target:
                h = mid-1
            else:
                l = mid +1
        return -1
            
        