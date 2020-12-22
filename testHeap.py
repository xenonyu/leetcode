import heapq

heap = [4, 3, 2]
heapq.heapify(heap)
print(heap)
heapq.heappush(heap, 1)
heapq.heappush(heap, 5)
heapq.heappush(heap, 3)
heapq.heappush(heap, 2)
heapq.heappush(heap, 7)
heapq.heappush(heap, 1)
print(heap)
for i in range(len(heap)):
    print(heapq.heappop(heap))
