T = int(input())
ans = ""
for test_case in range(1, T+1):
    now = test_case
    yes = 0  # 각 자리수가 3,6,9 숫자인 경우 개수를 셈
    no = 0  # 각 자리수가 3, 6, 9를 제외한 숫자인 경우를 셈
    while test_case >= 1:
        x = test_case % 10
        if x == 3 or x == 6 or x == 9:
            yes += 1
        else:
            no += 1
        test_case = test_case // 10  # 몫 연산을 통해 다음 연산할 숫자 갱신

    if yes == 0:
        ans += str(now)
    else:
        ans += str("-"*yes)
    ans += " "

print(ans)