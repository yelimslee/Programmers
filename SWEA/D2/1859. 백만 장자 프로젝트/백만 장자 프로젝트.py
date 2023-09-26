T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    li = list(map(int, input().split()))

    # 뒤에서 부터 편하게 탐색하기 위해 문자열 전체 역순화
    li = li[::-1]
    profit = 0
    curr = li[0]
    for i in range(1, N):
        if curr > li[i]:
            profit += (curr - li[i])
        else:
            curr = li[i]

    print(f'#{test_case} {profit}')