# 행: len(set(lst)) != 9: return
# 열: arr1 = list(zip(*arr))
# block: 3*3, for i (0,9,3) for j (0,3,6)
def solve():
    for lst in arr:
        if len(set(lst)) != N:
            return 0
        
    arr1 = list(zip(*arr))
    for lst in arr1:
        if len(set(lst)) != N:
            return 0
        
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            lst = arr[i][j:j+3] + arr[i+1][j:j+3] +arr[i+2][j:j+3]
            if len(set(lst)) != N:
                return 0
    return 1
T = int(input())
for test_case in range(1, T+1):
    N = 9
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = solve()
    print(f"#{test_case} {ans}")