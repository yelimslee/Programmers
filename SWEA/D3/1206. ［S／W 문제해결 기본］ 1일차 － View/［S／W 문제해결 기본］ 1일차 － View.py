# 좌/우 2칸 최대값 찾음 -> 내 높이가 > 최대값 => 차이만큼 누적

T = 10
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    ans = 0
    for i in range(2, N-2):
        max = lst[i-2]
        for j in range(i-1, i+3):
            if j == i:
                continue
            else:
                if max < lst[j]:
                    max = lst[j]
        if lst[i] > max:
            ans += lst[i] - max
    print(f"#{test_case} {ans}")