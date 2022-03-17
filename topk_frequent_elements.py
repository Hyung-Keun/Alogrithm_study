import collections
import heapq
def topKFrequent(nums, k):
    freqs =  collections.Counter(nums) #모듈로 빈도계산
    freqs_heap = [] #

    for f in freqs:
        heapq.heappush(freqs_heap, (-freqs[f], f))

    topk = list()
    for _ in range(k):
        topk.append(heapq.heappop(freqs_heap)[1])

    return topk


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topKFrequent(nums, k))