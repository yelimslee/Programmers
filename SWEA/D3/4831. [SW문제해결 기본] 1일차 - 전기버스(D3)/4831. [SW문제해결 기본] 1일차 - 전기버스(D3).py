T = int(input())
for test_case in range(1, T+1):
    K, N, M = map(int, input().split())
    lst = [0] + list(map(int, input().split())) + [N]

    ans = start = 0
    for i in range(1, M+2):
        if lst[i] - lst[i-1] > K:
            ans = 0
            break
        if lst[i] - start > K:
            start = lst[i-1]
            ans += 1

    print(f"#{test_case} {ans}")