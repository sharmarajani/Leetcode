class Solution:

    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7
        h_edges = self.get_edges(hFences, m)
        v_edges = self.get_edges(vFences, n)

        max_edge = max(h_edges & v_edges, default=0)
        return (max_edge * max_edge) % MOD if max_edge else -1
    def get_edges(self, fences: List[int], border: int) -> set:
        points = sorted([1] + fences + [border])
        return {
            points[j] - points[i]
            for i in range(len(points))
            for j in range(i + 1, len(points))
        }
        # if not (hFences or vFences): return -1
        # # if len(hFences)< 2 or len(vFences)<2:
        # #     return -1
        # hmax, vmax, hcur, vcur =1,1,1,1
        # hFences.sort()
        # vFences.sort()
        # for i in range(1,len(hFences)):
        #     if hFences[i-1]+1 ==hFences[i]:
        #         hcur+=1
        #     else:
        #         hcur=1
        #     hmax=max(hcur, hmax)
        # for i in range(1,len(vFences)):
        #     if vFences[i-1]+1==vFences[i]:
        #         vcur+=1
        #     else:
        #         vcur=1
        # vmax=max(vcur, vmax)
        # side = min(hmax, vmax) +1
        # return side * side

        
   
        