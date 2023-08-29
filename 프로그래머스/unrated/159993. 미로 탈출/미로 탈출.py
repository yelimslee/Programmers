from collections import deque

def solution(maps):
    answer = 0
    
    # 미로 크기부터 찾아야 돼
    rows = len(maps)
    columns = len(maps[0])
    
    #시작 지점('S')을 찾아서 어딘가에 좌표를 저장합시다
    for i in range(rows):
        for j in range(columns):
            if maps[i][j] == 'S':
                sx, sy = i, j
    
    # 레버는 안 당긴 상태
    lever = False
    
    # 방문지 2개
    visited = [] # 레버 안 당긴 방문지
    visited_l = [] # 레버 당긴 후의 방문지
    
    for i in range(rows):
        visited.append([False] * columns)
        visited_l.append([False] * columns)
    
    # 큐 자료 구조 만들어야 함 시작 지점(시작하는 x좌표, 시작하는 y좌표)이랑, 움직인 거리, 레버
    queue = deque([[sx, sy, 0, lever]])
    
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    
    while queue:
        
        x, y, time, lever = queue.popleft()
        
        # 레버 사용하지 않은 상태
        if not lever:
            visited[x][y] = True
        else:
            visited_l[x][y] = True
            
        
        # 만약에 현재 위치가 레버
        if maps[x][y] == 'L':
            lever = True
            visited_l[x][y] = True
            
        # 레버 사용했어, 현재 위치가 출구야, visited_l에도 방문 여부가 체크가 되어 있는 상태인 경우
        if lever and maps[x][y] == 'E' and visited_l[x][y]:
            return time
        
        for d in directions:
            row_x = x + d[0]
            row_y = y + d[1]
            
            if 0 <= row_x < rows and 0 <= row_y < columns:
                
                if not lever:
                    # 다음에 인접한 노드가 방문하지 않았고 벽이 아니면
                    if not visited[row_x][row_y] and maps[row_x][row_y] != 'X':
                        visited[row_x][row_y] = True
                        queue.append([row_x, row_y, time + 1, lever])
                else:
                    if not visited_l[row_x][row_y] and maps[row_x][row_y] != 'X':
                        visited_l[row_x][row_y] = True
                        queue.append([row_x, row_y, time + 1, lever])
                    
    # while문 다 돌았어 다 돌고 나왔는데 time을 반환 못했네?
    # 탈출 못해서 미로 안에서 굶어 죽은 상태
    return -1