def solution(n, computers):
    count = 0
    visited = [False] * n  # 모든 노드가 방문되지 않은 상태로 초기화된 방문 노드 목록

    def dfs(vertex):
        visited[vertex] = True  # 현재 노드를 방문한 것으로 표시
        for idx in range(n):
            if computers[vertex][idx] == 1 and not visited[idx]:
                dfs(idx)  # 인접한 미방문 노드를 재귀적으로 방문

    for node in range(n):  # 모든 노드를 반복
        if not visited[node]:  # 노드가 방문되지 않았다면 새로운 DFS를 시작
            dfs(node)
            count += 1  # 새로운 연결된 구성 요소가 발견될 때마다 카운트 증가

    return count  # 연결된 구성 요소의 개수를 반환
