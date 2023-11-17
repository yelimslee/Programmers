# 깊이우선탐색
# 탐색할 때마다 칼로리가 넘어가면 탐색을 수행하지 않고 
# 기존에 저장된 최대 맛보다 크면 갱신 과정을 거침
def dfs(index, sTaste, sKcal):
    global maxTaste

    #총 칼로리를 넘으면 리턴
    if sKcal > L:
        return
    
    #taste의 합이 제일 큰 taste합보다 크면 갱신
    if maxTaste < sTaste:
        maxTaste = sTaste

    # 햄버거 재료 데이터를 다 돌면 리턴
    if index == N:
        return
    
    # index 파라미터를 통해 taste, kcal 대입
    taste, kcal = data[index]

    # 햄버거 재료 리스트에서 재료를 사용했을 때
    dfs(index+1, sTaste+taste, sKcal+kcal)
    # 햄버거 재료 리스트에서 재료를 사용하지 않았을 때
    dfs(index+1, sTaste, sKcal)

T = int(input())
for testcase in range(1, T+1):
    N,L = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    maxTaste = 0
    dfs(0,0,0)
    print(f"#{testcase} {maxTaste}")