T= int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    lst = lst[::-1]
    profit = 0
    curr = lst[0]
    for i in range(1, N):
        if curr > lst[i]:
            profit += curr - lst[i]
        else:
            curr = lst[i]
    print(f"#{test_case} {profit}")