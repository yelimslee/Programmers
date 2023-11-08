def dfs(c):
    global ans

    ans += 1
    v[c] = 1

    for n in adj[c]:            # c와 연결된 노드 모두 처리
        if not v[n]:
            dfs(n)

N = int(input())
M = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

ans = 0
v = [0]*(N+1)
dfs(1)
print(ans-1)