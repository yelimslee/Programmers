def solution(n, results):
    answer = 0

    # 그래프 초기화
    graph = [[False] * (n + 1) for _ in range(n + 1)]

    # 경기 결과를 그래프에 반영
    for a, b in results:
        graph[a][b] = True

    # 플로이드-와샬 알고리즘을 사용하여 모든 선수간의 승패 여부를 확인
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = True

    # 각 선수에 대해 순위를 정확하게 매길 수 있는지 확인
    for i in range(1, n + 1):
        # 현재 선수가 다른 모든 선수와의 승패 관계를 검사할 때 이긴 횟수와 진 횟수를 세는데 사용
        count = 0
        for j in range(1, n + 1):
            # 선수 i와 선수 j 사이의 경기 결과를 확인
            if graph[i][j] or graph[j][i]:
                # 선수 i가 선수 j에게 승리하거나 패배한 경우 count 증가
                count += 1

        # 모든 선수 j에 대해 반복하면, 
        # 현재 선수 i가 몇 번 승리하거나 패배했는지를 count 변수에 저장할 수 있게 됨
        # n - 1은 자기 자신을 제외한 모든 선수의 수
        # count가 n - 1과 같다면 현재 선수 i의 순위를 정확하게 매길 수 있다는 의미
        if count == n - 1:
            # 그래서 최종적으로 answer에 카운트
            answer += 1

    return answer
