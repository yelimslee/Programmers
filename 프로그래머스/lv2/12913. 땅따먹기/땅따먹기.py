def solution(land):
    
    # land 배열의 행의 개수를 구함
    row_count = len(land)
    
    # 동적계획법을 위한 2차원 배열(table)을 초기화
    # 첫 번째 행은 land의 첫 번째 행과 동일하게 설정
    table = [land[0]]
    
    # 나머지 행은 0으로 채워진 배열을 추가
    # table.extend([[0] * 4 for _ in range(row_count -1)])
    for idx in range(1, len(land)):
        table.append([0] * 4)
        
    # 동적 계획법 수행
    # 1번째 행부터 마지막 행까지 순회하면서 계산을 진행함
    for i in range(1, row_count):
        for j in range(4):
            # 같은 열은 선택할 수 없으므로, j를 제외한 나머지 열의 인덱스를 구현
            other_columns = [idx for idx in range(4) if idx != j]
            a, b, c = other_columns
            
            # 현재 위치의 점수는 land 배열의 해당 위치 값과 이전 행에서 가능한 최대 점수의 합
            table[i][j] = land[i][j] + max(table[i-1][a], table[i-1][b], table[i-1][c])
                                           
    # 마지막 항의 최대 값 반환
    return max(table[-1])