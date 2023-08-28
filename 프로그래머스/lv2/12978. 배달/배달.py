from collections import deque

def solution(N, road, K):
    
    answer = 0
    
    graph = []
    
    for i in range(N+1):
        graph.append([])
    
    for start, next, time in road:
        graph[start].append((next, time))
        graph[next].append((start, time))

    road_time = [float('inf')] * (N + 1)
    
    road_time[1] = 0

    queue = deque([(1,0)])
    
    
    while queue:
        current_town, current_time = queue.popleft()
        
        for dilivery_town, time in graph[current_town]:
            dilivery_time = current_time + time

            if dilivery_time < road_time[dilivery_town]:
                road_time[dilivery_town] = dilivery_time
                queue.append((dilivery_town, dilivery_time))
    
    
    for i in road_time:
        if i <= K:
            answer += 1
    

    return answer