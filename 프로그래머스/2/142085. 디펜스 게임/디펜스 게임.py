import heapq

def solution(n, k, enemy):
    heap = []  # 최소 힙
    for i, e in enumerate(enemy):
        heapq.heappush(heap, e)
        
        if len(heap) > k:
            n -= heapq.heappop(heap)  
        if n < 0:  # 병사가 모자라면 종료
            return i
    return len(enemy)
