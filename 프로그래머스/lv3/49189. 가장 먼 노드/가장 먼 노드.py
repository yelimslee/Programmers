from collections import deque

def solution(n, edge):
    
    answer = 0
    graph = []
    
    for i in range(n + 1):
        graph.append([])
        
    for e in edge:
        start, end = e
        graph[start].append(end)
        graph[end].append(start)

    visited = [False] * (n + 1)

    distances = [0] * (n + 1)

    queue = deque([(1, 0)])

    visited[1] = True

    while queue:
        vertex, distance = queue.popleft()

        distances[vertex] = distance

        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True

                queue.append((neighbor, distance + 1))

    for distance in distances:
        if distance == max(distances):
            answer += 1

    return answer