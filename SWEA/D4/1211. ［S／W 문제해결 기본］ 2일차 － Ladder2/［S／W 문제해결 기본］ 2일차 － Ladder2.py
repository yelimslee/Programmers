T = 10
for test_case in range(1, T+1):
    _ = int(input())
    arr = [[0] + list(map(int, input().split())) +[0] for _ in range(100)]

    min = 100*100
    for sj in range(1, 101):
        if arr[0][sj] == 0:
            continue
    
        cj = sj
        cnt = dr = ci = 0
        while ci < 99:
            cnt += 1
            if dr == 0:  # 이동
                ci += 1
                if arr[ci][cj-1] == 1:  # 방향 전환
                    dr -= 1
                elif arr[ci][cj+1] == 1:
                    dr = 1
            else:  # 좌/우
                cj += dr
                if arr[ci][cj+dr] == 0:
                    dr = 0
        if min >= cnt:
            min = cnt
            ans = sj-1


    print(f"#{test_case} {ans}")