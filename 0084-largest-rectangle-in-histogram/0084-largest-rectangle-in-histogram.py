class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, area = [[heights[0], 0]] , 0
        for i in range(1, len(heights)):
            start = i
            while stack and stack[-1][0]> heights[i]:
                val, idx=stack.pop()
                area = max ( area, val * (i -idx))
                start=idx
            stack.append([heights[i], start])
        
        while stack :
            val, idx=stack.pop()
            area = max(area, val *(len(heights)-idx) )
        return area

        