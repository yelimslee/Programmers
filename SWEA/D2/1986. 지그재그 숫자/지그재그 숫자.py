T= int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = []
    sum = 0

    for i in range(1, N+1):
        #홀수
        if i % 2 == 1:
            lst.append(i)
        # 짝수
        else:
            lst.append(-i)
    for j in lst:
        sum += j

    print(f"#{test_case} {sum}")