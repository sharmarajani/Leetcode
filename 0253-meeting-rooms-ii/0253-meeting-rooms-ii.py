class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        min_heap = []
        used_room = 0
        intervals.sort(key= lambda x: x[0])
        heapq.heappush(min_heap, intervals[0][1])
        for i in range(1, len(intervals)):
            if min_heap[0] <= intervals[i][0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, intervals[i][1])
        return len(min_heap)
