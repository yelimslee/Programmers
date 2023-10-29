#한 번에 많은 양을 사재기 할 수 없음
#하루에 최대 1만큼 구입할 수 있음(1구입 또는 0구입)
#판매는 얼마든지 할 수 있음

# 뒤에서 순회, O(n)
# 첫인덱스: max, 그 다음 수가 작으면 max-list[i]만큼 누적, 크면 max갱신
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    li = list(map(int, input().split()))

    # 뒤에서 부터 편하게 탐색하기 위해 문자열 전체 역순화
    li = li[::-1]
    profit = 0
    curr = li[0]
    for i in range(1, N):
        if curr > li[i]:
            profit += (curr - li[i])
        else:
            curr = li[i]

    print(f'#{test_case} {profit}')



#2번째 방법 처음부터 순회(시간이 오래걸림) O(n²)
#처음부터 가장 큰 수 전까지 구매, 큰 수에서 판매
#->큰수 다음부터 끝까지 위 동작을 반복
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    ans = 0
    while s < N:
        for i in range(s+1, N):
            i_max = s
            if lst[i_max] < lst[i]:
                i_max = i
        for i in range(s, i_max):
            ans += (lst[i_max] - lst[i])
        s = i_max + 1

    print(f"#{test_case} {ans}")
