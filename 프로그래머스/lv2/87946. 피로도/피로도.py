from itertools import permutations

def solution(k, dungeons):
    answer = 0  # 최대로 통과할 수 있는 던전 수를 저장하는 변수
    
    # 모든 가능한 던전 순열을 생성하고 각각에 대해 검사
    for p in permutations(dungeons, len(dungeons)):
        tmp = k  # 남은 에너지를 나타내는 변수 초기화
        cnt = 0  # 현재 순열에서 통과한 던전 수 초기화
        
        # 현재 순열에서 각 던전에 대해 반복
        for need, spend in p:
            if tmp >= need:  # 충분한 에너지가 있을 때
                tmp -= spend  # 던전을 통과하고 남은 에너지 계산
                cnt += 1  # 통과한 던전 수 증가
        answer = max(answer, cnt)  # 현재까지의 최대 통과 던전 수 업데이트
        
    return answer  # 최대 통과 던전 수를 반환