# N행으로 진행 -> 성공, ans += 1
# 0행부터 Q 놓고, 다음줄로 진행 (Q를 놓는 게 가능한지 CKECK!)
# 열이 가능한지 확인, v1[j] = 1
# 오른쪽 대각선이 가능한지 확인, v2[i+j]=1
# 왼쪽 대각선이 가능한지 확인, v3[i-j]=1
# n: 행 번호, j: 열 번호

def dfs(n):
    global ans
    if n == N:
        ans += 1
        return 
    
    for j in range(N):
        if v1[j] == v2[n+j] == v3[n-j] == 0:
            v1[j] = v2[n+j] = v3[n-j] = 1
            dfs(n+1)
            v1[j] = v2[n+j] = v3[n-j] = 0

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    ans = 0

    v1, v2, v3 = [[0]*(2*N) for _ in range(3)]
    dfs(0)
    print(f"#{test_case} {ans}")