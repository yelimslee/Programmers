def solution(s):
    answer = True
    
    # '('을 담을 스택
    my_stack = []
    
    # s순회: string은 리스트처럼 요소 순회가 가능
    # : 다른 프로그래밍 언어도 마찬가지
    for i in s:
        # 스택에 '('을 담을 거
        if i == '(':
            my_stack.append(i)
        
        # s에 ')'인 경우
        else:
            if not my_stack:
                return False
            else:
                my_stack.pop()
                
    # for문 다 순회했는데 무언가 들어있으면 결국 짝이 안 맞는다는 것
    print(my_stack)
    print(bool(my_stack))
    
    if my_stack:
        answer = False
        
    return answer