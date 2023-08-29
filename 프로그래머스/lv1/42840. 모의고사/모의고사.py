def solution(answers):
    answer = []
    
    #수포자 3명 찍는 방식이 순환되는 기준을 담음
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    #점수 담을 부분
    scores = [0, 0, 0]
    
    #answer의 길이로 순회
    for i in range(len(answers)):
        #학생 답이 더 길 수 있으니까 저걸 어떻게 늘려간담
        
        #i % len(student1) : 현재 문제의 인덱스 i를 수포자 1의 패턴 길이로 나눈 나머지
		#이렇게 함으로써 수포자 1은 패턴을 반복하면서 문제를 푸는 효과
		# 0 % 10 = 0 / 1 % 10 = 
        
        if student1[i % len(student1)] == answers[i]:
            scores[0] += 1

        if student2[i % len(student2)] == answers[i]:
            scores[1] += 1

        if student3[i % len(student3)] == answers[i]:
            scores[2] += 1
    
    max_score = max(scores)
    
    for i in range(len(scores)):
        if max_score == scores[i]:
            answer.append(i + 1)  # 가장 많이 맞춘 수포자의 번호를 추가
    
    return answer
