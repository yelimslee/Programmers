# sys 모듈을 사용하기 위해 import합니다.
import sys

# 입력을 빠르게 받기 위해 sys.stdin.readline을 사용합니다.
input = sys.stdin.readline

# 재귀 깊이 제한을 확장해주기 위한 코드입니다. 
# DFS 탐색 시에 깊이가 매우 깊어질 경우를 대비하기 위해서입니다.
sys.setrecursionlimit(10**8)

# 정답 문자열로 사용할 변수입니다. 초기값으로 z를 지정하여 최소값을 찾기 위한 기준으로 설정하였습니다.
answer = "z"
    

def solution(n, m, x, y, r, c, k):
    """
    맨하탄 거리 설명 - https://ko.wikipedia.org/wiki/%EB%A7%A8%ED%95%B4%ED%8A%BC_%EA%B1%B0%EB%A6%AC
    
    dist > k:

    이 조건은 맨해튼 거리(최소 이동 횟수)가 주어진 k(최대 이동 횟수)보다 크다는 것을 의미합니다. 따라서 주어진 횟수 안에 목적지에 도달할 수 없다는 것을 나타냅니다. 예를 들어, 목적지까지 최소 5번 움직여야 하는데 주어진 이동 횟수가 4라면, 목적지에 도달할 수 없습니다.
    
    (k - dist) % 2 == 1:

    이 조건은 약간 더 복잡합니다. 먼저 k - dist는 추가로 사용할 수 있는 이동 횟수를 나타냅니다. 예를 들어, 목적지까지 5번 움직여야 하는데 주어진 이동 횟수가 7이라면, 추가로 2번 움직일 수 있습니다.

    이제, 추가로 움직일 수 있는 횟수가 홀수인지 확인합니다. 홀수인 경우, 문제의 제약 사항에 따라 목적지에 도달할 수 없습니다. 왜냐하면 맨해튼 거리를 기반으로 최소 이동 횟수로 목적지에 도달했을 때, 추가로 홀수 번 움직이면 목적지에서 벗어나게 됩니다. 그리고 이후에 다시 목적지로 돌아올 수 없습니다. 반면에 추가 이동 횟수가 짝수라면, 이동 후 다시 원래 위치로 돌아올 수 있기 때문에 문제가 없습니다.

    예를 들어, 추가로 1번 움직일 수 있는 경우, 한 번 움직이면 목적지에서 벗어나지만 다시 원래 위치로 돌아올 수 없습니다. 하지만 추가로 2번 움직일 수 있다면, 한 번 움직여 목적지에서 벗어나고 다시 원래 위치로 돌아올 수 있습니다.
    """
    
    # x, y 좌표의 변화를 나타내기 위한 리스트입니다.
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]

    # 해당 방향을 문자로 표현하기 위한 리스트입니다.
    dAlpha = ['d', 'l', 'r', 'u']

    # 시작 위치에서 목적지까지의 맨해튼 거리를 계산합니다.
    dist = abs(x - r) + abs(y - c)
    
    # 맨해튼 거리가 k보다 크거나, k와 맨해튼 거리의 차이가 홀수면 도달이 불가능합니다.
    if dist > k or (k - dist) % 2 == 1:
        return "impossible"

    # 주어진 좌표가 보드 내부에 있는지 검사하는 함수입니다.
    def isVaild(nx, ny, n, m):
        return 1 <= nx and nx <= n and 1 <= ny and ny <= m

    # DFS 탐색을 수행하는 함수입니다.
    def dfs(n, m, x, y, r, c, prev_s, cnt, k):
        # 전역 변수 answer를 사용하기 위해 global 키워드를 사용합니다.
        global answer

        # 현재 위치에서 목적지까지의 최소 이동 횟수보다 남은 횟수가 작으면 더 이상 탐색하지 않습니다.
        if k < cnt + abs(x - r) + abs(y - c):
            return

        # 목적지에 도달하고 이동 횟수가 k와 같으면 정답 문자열을 갱신합니다.
        if x == r and y == c and cnt == k:
            answer = prev_s
            return

        # 4가지 방향으로의 이동을 시도합니다.
        for i in range(4):
            # 다음 좌표를 계산합니다.
            nx, ny = x + dx[i], y + dy[i]

            # 다음 좌표가 보드 내부에 있고, 현재의 경로가 정답보다 짧으면 DFS 탐색을 계속합니다.
            if isVaild(nx, ny, n, m) and prev_s < answer:
                dfs(n, m, nx, ny, r, c, prev_s+dAlpha[i], cnt + 1, k)
    
    # DFS 탐색을 시작합니다.
    dfs(n, m, x, y, r, c, "", 0, k)

    # 탐색 결과인 answer를 반환합니다.
    return answer