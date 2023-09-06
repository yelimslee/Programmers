def solution(n):
    # dp 배열을 초기화. 배열의 크기는 n+1 또는 2 중에서 더 큰값으로 설정
    table = [0] * max(n + 1, 2)
    
    # 1개의 타일은 세로로 1개만 가능하고, 2개의 타일은 가로로 2개, 세로로 2개 총 2가지 경우
    table[0], table[1] = 1, 1
    
    # 2부터 n까지의 피보나치 값을 계산
    # 각 숫자 i에 대한 피보나치 값은 table[i-2] + table[i-1]로 구할 수 있음
    for i in range(2, n+1):
        table[i] = (table[i-2] + table[i-1]) % 1000000007
    
    # 마지막으로 table[n]이 n번째 타일을 놓을 수 있는 경우의 수
    return table[n]