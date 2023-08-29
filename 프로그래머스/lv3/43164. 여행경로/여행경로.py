def solution(tickets):
    airports = {}  # key: 출발 공항, value: 도착할 수 있는 공항들의 리스트

    for start, end in tickets:
        if start not in airports:
            airports[start] = []
        airports[start].append(end)
    
    # 알파벳 역순으로 정렬
    for key in airports:
        airports[key].sort(reverse=True)
    
    total_tickets = len(tickets)
    current_path = []
    
    dfs(airports, total_tickets, current_path, "ICN", 0)
    
    return current_path

def dfs(airports, total_tickets, current_path, current_airport, used_tickets):
    """
    :param airports: 딕셔너리 형태로 각 출발 공항에서 도착할 수 있는 공항들의 리스트를 저장
    :param total_tickets: 전체 티켓 수
    :param current_path: 현재까지의 여행 경로를 저장하는 리스트
    :param current_airport: 현재 위치한 공항
    :param used_tickets: 지금까지 사용한 티켓의 수
    """
    
    # 현재 공항을 경로에 추가
    current_path.append(current_airport)
    
    # 모든 티켓을 사용했다면 종료
    if used_tickets == total_tickets:
        return True
    
    if current_airport not in airports:
        current_path.pop()
        return False
    
    # 현재 공항에서 이동할 수 있는 다음 공항들을 순회
    for idx in range(len(airports[current_airport])):
        next_airport = airports[current_airport].pop()  # 마지막 요소 선택
        
        # 다음 공항으로 이동할 수 있다면
        if dfs(airports, total_tickets, current_path, next_airport, used_tickets + 1):
            return True
        
        # 실패했을 경우 원래대로 복구
        airports[current_airport].insert(0, next_airport)
    
    # 모든 경로를 탐색했지만 실패했을 경우 경로에서 현재 공항 제거
    current_path.pop()
    return False