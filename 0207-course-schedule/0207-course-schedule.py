class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hmap = defaultdict(list)
        inbound = [0] * numCourses
        cnt = 0
        q= deque()
        for i in prerequisites:
            hmap[i[1]].append(i[0])
            inbound[i[0]]+=1
        
        for i in range(numCourses):
            if inbound[i] ==0:
                cnt+=1
                q.append(i)
        if cnt == numCourses:
            return True
        if not q:
            return False
        
        while q:
            idx = q.popleft()
            if hmap[idx]:
                for i in hmap[idx]:
                    inbound[i] -=1
                    if inbound[i] == 0:
                        q.append(i)
                        cnt+=1
                    if cnt == numCourses:
                        return True
        return False
                    
            

        