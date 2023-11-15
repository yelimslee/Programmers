T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    avg = sum(lst)/N
    cnt = 0

    for j in lst:
        if j <= avg:
            cnt += 1

    print(f"#{testcase} {cnt}")