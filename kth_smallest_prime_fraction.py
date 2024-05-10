import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:

        pq = []

        for i in range(len(arr)): 
            heapq.heappush(pq, ((arr[i] / arr[-1]), i, len(arr)-1))
        
        for i in range(k-1): 
            fraction, start, end = heapq.heappop(pq)
            if start < end: 
                heapq.heappush(pq, (arr[start] / arr[end-1], start, end-1))
        
        ans = heapq.heappop(pq)
        return [arr[ans[1]], arr[ans[2]]]