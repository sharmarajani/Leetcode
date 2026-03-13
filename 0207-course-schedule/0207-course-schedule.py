class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        q=deque()
        hmap=defaultdict(list)
        inbound =[0] * numCourses

        count=0
        for i in prerequisites:
            inbound[i[0]] +=1
            # if i[1] not in hmap:
            #     hmap[i[1]] =[]
            hmap[i[1]].append(i[0])
        
        for i in range(numCourses):
            if inbound[i]==0:
                count+=1
                q.append(i)
            
        if count ==numCourses:
            return True
        if not q:
            return False

        while q:
            curr= q.popleft()
            dependency=hmap[curr]
            if dependency:
                for i in dependency:
                    inbound[i]-=1
                    if inbound[i]==0:
                        q.append(i)
                        count+=1
                    if count == numCourses:
                        return True
        return False



        