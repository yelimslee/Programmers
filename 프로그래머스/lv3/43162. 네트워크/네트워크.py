def solution(n, computers):
    # 결과를 담을 변수, 결국 남아있는 네트워크를 여기 저장함.
    count = 0
    # 실제 방문 여부를 체크할 수 있는 불리언 값을 가진 리스트. 항상 이걸 체크하면서 방문여부를 확인.
    visited = [False] * n  # [False, False, False]
    # visited = [False for _ in range(0, n)]
    
    def dfs(vertex):  # 수정: 변수 이름이 1이 아니라 vertex여야 함
        #더 이상 도달할 곳이 없는 경우 -> 단순히 반복이 끝났을 경우
        visited[vertex] = True
        
        for idx in range(n):
            if computers[vertex][idx] == 1 and visited[idx] == False:
                dfs(idx)
    
    for vertex in range(n):  # 수정: 변수 이름이 2가 아니라 vertex여야 함
        if visited[vertex] == False:
            dfs(vertex)
            count += 1
    
    return count