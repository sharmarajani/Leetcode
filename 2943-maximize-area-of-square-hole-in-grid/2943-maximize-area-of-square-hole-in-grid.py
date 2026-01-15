class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        hmax,vmax, hcur, vcur =1,1,1,1
        for i in range(1, len(hBars)):
            if hBars[i] == hBars[i-1]+1:
                hcur +=1
            else:
                hcur =1
            hmax = max(hcur, hmax)

        for i in range(1, len(vBars)):
            if vBars[i] == vBars[i-1]+1:
                vcur +=1
            else:
                vcur =1
            vmax = max(vcur, vmax)
        side = min(vmax, hmax)  + 1
        return side * side
        