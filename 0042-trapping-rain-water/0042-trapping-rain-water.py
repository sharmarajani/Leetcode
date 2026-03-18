class Solution:
    def trap(self, height: List[int]) -> int:
        l, r , lw, rw = 0,len(height)-1,0, 0
        area = 0
        while l < r:
            if height[l] < height[r]:
                if height[l] < lw:
                    area += lw - height[l]
                else:
                    lw = height[l]
                l+=1
            else:
                if height[r] < rw:
                    area+= rw -height[r]
                else:
                    rw = height[r]
                r-=1
        return area



        