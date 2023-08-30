def solution(n, times):
    left = 1
    right = max(times) * n
    answer = 0
    
    # 탐색
    while left <= right:
        mid = (left + right) // 2
        
        total = 0
        for num in times:
            total += mid // num 
        # total = sum(mid // time for time in times)
    
        if total >= n:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1
        
    return answer