from sortedcontainers import SortedList

a = [5, 3, 1]
sl = SortedList()

for x in a:
    sl.add(x)

print(sl)
