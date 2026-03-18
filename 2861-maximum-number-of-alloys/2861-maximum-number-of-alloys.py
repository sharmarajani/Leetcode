class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        
        def can_make (target, machine_comp):
            total_cost= 0
            for i in range(n):
                needed = machine_comp[i] * target
                need_to_buy = max(0, needed - stock[i])
                total_cost += need_to_buy * cost[i]
                if total_cost > budget:
                    return False
            return True
        max_alloys = 0
        for machine in composition:
            low, hi = 0, 400000000
            while low <=hi:
                mid = (low + hi)//2
                if can_make(mid, machine):
                    best_for_this_machine = mid
                    low = mid +1
                else:
                    hi = mid-1
            max_alloys = max(max_alloys, best_for_this_machine)
        return max_alloys
        

        