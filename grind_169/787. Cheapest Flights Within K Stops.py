import collections
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(dict)
        for _from, _to, price in flights:
            graph[_from][_to] = price
        pq = [(0, src, 0)]
        vis = [math.inf] * n
        while pq:
            weight, city, cnt = heapq.heappop(pq)
            if city == dst and cnt - 1 <= k:
                return weight
            if vis[city] > cnt:
                vis[city] = cnt
                for adj_city, dw in graph[city].items():
                    heapq.heappush(pq, (weight + dw, adj_city, cnt + 1))
        return -1


# Dijkstra
# TC: O(N + E * k * log(EK))
# SC: (N + E * K)
# pq sort by weight, check cnt -1 <= k


import copy


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        costs = [math.inf] * n
        costs[src] = 0

        for i in range(k + 1):
            pre_costs = copy.deepcopy(costs)
            for start, end, price in flights:
                if pre_costs[start] != math.inf:
                    costs[end] = min(pre_costs[start] + price, costs[end])
        return costs[dst] if costs[dst] != math.inf else -1


# Bellman Ford
# TC: ((N + E) * k), iterating O(K*E) + swap distance array O(K*N)
# SC: O(N)
# note that we use deepcopy pre_costs =  copy.deepcopy(costs)

import collections
from sortedcontainers import SortedList


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(dict)
        for _from, _to, price in flights:
            graph[_from][_to] = price
        sl = SortedList(key=lambda x: -x[0])
        sl.add((0, src, 0))
        vis = [math.inf] * n
        while sl:
            weight, city, cnt = sl.pop()
            if city == dst and cnt - 1 <= k:
                return weight
            if vis[city] > cnt:
                vis[city] = cnt
                for adj_city, dw in graph[city].items():
                    sl.add((weight + dw, adj_city, cnt + 1))
        return -1

# Dijkstra
# TC: O(N + E * k * log(EK))
# SC: (N + E * K)
# replace pq to sortedList
