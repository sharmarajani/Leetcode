class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hmap = defaultdict(list)
        for i, num in enumerate(numbers):
            if (num) in hmap:
                return [ hmap[num][0] + 1 , i+1]
            hmap[target - num].append(i)
        return -1
            
            

        