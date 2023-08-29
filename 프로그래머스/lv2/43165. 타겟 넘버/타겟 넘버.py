def solution(numbers, target):
    def dfs(level, current_sum, answer):
        # 탈출 조건 (레벨이 numbers의 길이와 같거나 클 경우)
        if level >= len(numbers):
            # current_sum == target ->
            if current_sum == target:
                # answer += 1 더해야 함
                answer += 1
            # return answer
            return answer
        
        # 현재 숫자 = numbers[level] 를 더하거나, 빼는 경우 -> 재귀호출 해야함.
        # 재귀 호출할때, level은 모두 증가해야 함. 
        # 각 재귀 호출 결과를 갱신한 answer를 사용해야 함.
        answer = dfs(level + 1, current_sum + numbers[level], answer)
        answer = dfs(level + 1, current_sum - numbers[level], answer)
        return answer  # 결과를 반환해줘야 함.
    
    return dfs(0, 0, 0)
