def solution(prices):
    
    # prices 길이만큼 answer 길이 만듦
    answer = [0] * len(prices)
    
    # prices의 길이만큼 순회
    for i in range(len(prices)):
        # prices 다음 요소랑 계속 비교
        for j in range(i+1, len(prices)):
            # 이전 가격이 이후 가격보다 낮으면 
            if prices[i] <= prices[j]:
                # 1초 증가
                answer[i] += 1
            else:
                # 높아도 일단 1초는 버텼다고 생각해서 올리고
                answer[i] += 1
                # 멈춤
                break
    return answer