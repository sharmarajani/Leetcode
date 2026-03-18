class Solution:
    def trap(self, height: List[int]) -> int:
        l, r , lw, rw = 0,len(height)-1,0, 0
        area = 0
        while l <= r:
            if lw <=rw:
                # if height[l] < lw:
                #     area += lw - height[l]
                # else:
                #     lw = height[l]
                lw = max(lw, height[l] )
                area+= lw -height[l]
                l+=1
            else:
                # if height[r] < rw:
                #     area+= rw -height[r]
                # else:
                #     rw = height[r]
                rw = max(rw, height[r])
                area+= rw-height[r]
                r-=1
        return area



        