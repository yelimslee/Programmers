import heapq

def solution(scoville, K):

    answer = 0

    heap = []

    for i in scoville:
        heapq.heappush(heap, i)

    while heap[0] < K:

        if len(heap) == 1:
            return -1

        start_scoville = heapq.heappop(heap)

        next_scoville = heapq.heappop(heap) * 2

        mix_scoville = start_scoville + next_scoville

        answer += 1

        heapq.heappush(heap, mix_scoville)

    return answer