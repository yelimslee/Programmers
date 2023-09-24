T = int(input())
for i in range(1, T+1):
    list = map(int, input().split())
    answer = 0
    for j in list:
        if j % 2 ==1:
            answer += j
    print(f"#{i} {answer}")