class TimeMap:

    def __init__(self):
        self.hmap= defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        # print(self.hmap)
        if key not in self.hmap:
            return ""
        values = self.hmap[key]
        idx = bisect_right(values, [timestamp, chr(127)])
        if idx ==0:
            return ""
        return values[idx-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)