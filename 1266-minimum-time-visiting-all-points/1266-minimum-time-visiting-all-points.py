class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points)-1):
            x , y = points[i]
            tx, ty =points[i+1]
            ans += max((abs(tx-x), abs(ty-y) ))
        return ans