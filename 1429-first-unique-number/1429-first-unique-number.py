class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = deque(nums)
        self.hmap ={}
        for num in nums:
            if num not in self.hmap:
                self.hmap[num]=True
            else:
                self.hmap[num] = False
        # print(self.hmap)
        

    def showFirstUnique(self) -> int:
        while self.q and not self.hmap[self.q[0]] :
            self.q.popleft()
            # print(self.q)
        if not self.q:
            return -1
        else:
            return self.q[0]
        # print(self.q)
        
        

    def add(self, value: int) -> None:
        # self.q.append(value)
        if value not in self.hmap:
            self.hmap[value] = True
            self.q.append(value)
        else:
            self.hmap[value] = False
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)