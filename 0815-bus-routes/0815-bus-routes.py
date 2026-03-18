class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        hmap =defaultdict(list)
        if source == target:
            return 0
        q= deque()     
        visited_stops = {source}
        visited_buses = set()
        for i in range(len(routes)):
            if source in routes[i] and target in routes[i]:
                return 1
            for stop in routes[i]:
                hmap[stop].append(i)
                if stop ==source:
                    q.append((i,1))
                    visited_buses.add(i)

        cnt = 0
        while q:
            bus_no, cnt =q.popleft()
            visited_buses.add(bus_no)
            for stop in routes[bus_no]:
                if stop == target:
                    return cnt
                if stop not in visited_stops:
                    visited_stops.add(stop)
                # for values in  hmap[stops].values():
                #     if hmap[stops] not in visited:
                #         visited.add(stops)
                for next_bus in hmap[stop]:
                    if next_bus not in visited_buses:
                        visited_buses.add(next_bus)
                        q.append((next_bus, cnt+1))

        return -1

        