from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    deq1 = deque(queue1)  # deque 객체 생성
    deq2 = deque(queue2)  # deque 객체 생성
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    if (sum1 + sum2) % 2 != 0:
        return -1
    
    max_iterations = 4 * len(queue1) 
    
    while sum1 != sum2: 
        if answer == max_iterations:
            return -1

        if sum1 > sum2:
            one = deq1.popleft()
            deq2.append(one)
            sum2 += one
            sum1 -= one
        elif sum1 < sum2:
            two = deq2.popleft()
            deq1.append(two)
            sum1 += two
            sum2 -= two
        else:
            break 
           
        answer += 1

    return answer

