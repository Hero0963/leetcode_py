import collections


# N: len(routes), here N is total bus
# M: max_leng element in routes
# S: total bus stop
# TC: O(N * M + S * N)
# SC: O(S * N)


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        to_routes = collections.defaultdict(set)
        for i, route in enumerate(routes):
            for j in route:
                to_routes[j].add(i)

        bfs = [(source, 0)]
        visited_stop = set()
        visited_stop.add(source)
        for stop, bus_cnt in bfs:
            if stop == target:
                return bus_cnt
            for bus_idx in to_routes[stop]:
                bus = routes[bus_idx]
                for passing_stop in bus:
                    if passing_stop not in visited_stop:
                        bfs.append((passing_stop, bus_cnt + 1))
                        visited_stop.add(passing_stop)

                routes[bus_idx] = []  # clear bus stop

        return -1
