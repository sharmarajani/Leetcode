class UnionFind:
    def __init__(self, size):
        self.parent = [-1] * size
        self.rank = [0] * size
        self.count = 0

    def add_land(self, x):
        if self.parent[x] == -1:
            self.parent[x] = x
            self.count += 1
            return True
        return False

    def find(self, i):
        if self.parent[i] == i:
            return i
        # Path Compression: make nodes point directly to the root
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            # Union by Rank: attach the smaller tree under the larger tree
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_i] = root_j
                self.rank[root_j] += 1
            self.count -= 1

class Solution:
    def numIslands2(self, m, n, positions):
        uf = UnionFind(m * n)
        result = []
        for r, c in positions:
            idx = r * n + c
            if uf.add_land(idx):
                for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        neighbor_idx = nr * n + nc
                        if uf.parent[neighbor_idx] != -1:
                            uf.union(idx, neighbor_idx)
            result.append(uf.count)
        return result