# 10으로 나눴을 때, 3 6 9면 박수

N = int(input())
ans = ""
for i in range(1, N+1):
    now = i
    yes = 0  # 각 자릿수가 3,6,9 숫자인 경우의 갯수를 셈
    no = 0  # 각 자릿수가 3,6,9 를 제외한 숫자인 경우를 셈
    while i >= 1:
        r = i % 10  # 10으로 나눈 나머지
        if r == 3 or r == 6 or r == 9:
            yes += 1
        else:
            no += 1
        i = i//10  # 몫 연산을 통해 다음 연산할 숫자를 갱신

    if yes == 0:
        ans += str(now)
    else:
        ans += str("-"*yes)
    ans += " "

print(ans)