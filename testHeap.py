import heapq

heap = []
heapq.heappush(heap, 1)
heapq.heappush(heap, 5)
heapq.heappush(heap, 3)
heapq.heappush(heap, 2)
heapq.heappush(heap, 7)
heapq.heappush(heap, 1)
print(heapq.heappop(heap))  # -> 1
