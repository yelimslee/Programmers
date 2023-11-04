N = int(input())
ans = ""
for i in range(1, N+1):
    now = i
    yes = 0  # 3의 배수일 경우

    while i >= 1:
        r = i % 10
        if r ==3 or r == 6 or r == 9:
            yes += 1
        i = i//10

    if yes == 0:
        ans += str(now)
    else:
        ans += str("-"*yes)
    ans += " "

print(ans)