def solution(arr1, arr2):
    
		# 입력 행렬 arr1의 행과 열의 개수를 확인하기 위해 미리 계산
    rows = len(arr1)
    cols = len(arr1[0])
    
		# answer라는 빈 행렬을 생성 
		# 두 입력 행렬 arr1과 arr2의 크기와 같으며, 모든 원소를 0으로 초기화
    answer = [[0] * cols for _ in range(rows)]
    
		# 중첩된 반복문을 사용 (완전 탐색)
    for i in range(rows):
        for j in range(cols):
            answer[i][j] = arr1[i][j] + arr2[i][j]
 
    return answer