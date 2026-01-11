class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights)==0 or heights ==None:
            return 0
        stack =[[heights[0] , 0]]
        max_area = 0
        for i in range(1,len(heights)):
            start=i
            while stack and  heights[i] < stack[-1][0]:
                val, idx=stack.pop()
                max_area= max(max_area , val * (i-idx) )
                start = idx    
            stack.append([heights[i], start])

        for h, idx in stack:
            max_area = max(max_area, h * (len(heights)-idx))
        return max_area
            

        