import heapq

def k_naibolshiy(arr: list[int], k: int):
    heap = []
    for element in arr:
        heapq.heappush(heap, element)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]

arr = [3, 2, 1, 5, 6, 4]
k = 4
print(k_naibolshiy(arr, k))
