T = int(input())
for test_case in range(1, T+1):
    alp = (input())
    N = len(alp)
    s = N//2
    ans = 1

    for i in range(s):
        if alp[i] != alp[N-1-i]:
            ans = 0

    print(f"#{test_case} {ans}")