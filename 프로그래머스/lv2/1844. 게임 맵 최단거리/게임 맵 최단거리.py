from collections import deque

def solution(maps):
    answer = 0
    
    # 미로의 행과 열을 찾아서 그걸로 이차원 방문 배열을 만들 것임.
    rows = len(maps)  # 행
    columns = len(maps[0])  # 열
    
    visited = []
    
    # 미로 크기만큼 visited 이차원 배열 생성해야 돼서
    for i in range(rows):
        visited.append([False] * columns)
        
    # 상하좌우 이동 방향을 정의해줘야 함: 오른쪽, 왼쪽, 아래, 위
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    
    queue = deque([(0, 0, 1)])  # 마지막 1은 count 됐다라는 의미
    visited[0][0] = True
    
    while queue:
        x, y, count = queue.popleft()
        
        # 도착점에 도달했다면 count 반환 : index로 계산해야 함
        if x == rows - 1 and y == columns - 1:
            return count
        
        # 상하좌우 이동 검사
        for i in directions:
            row_x = x + i[0]
            column_y = y + i[1]  # 오타 수정: u -> y
            
            # 미로 범위 안에 있는지, 인접한 노드가 길인지 아닌지, 방문 했는지 안 했는지
            if 0 <= row_x < rows and 0 <= column_y < columns and not visited[row_x][column_y] and maps[row_x][column_y] == 1:
                # 방문 처리
                visited[row_x][column_y] = True
                # 큐에 추가
                queue.append((row_x, column_y, count + 1))  # 괄호 추가: tuple 형태
                
    # while 문을 다 돌고 나왔다는 의미
    # 상대 진영으로 갈 길이 없다
    return -1
