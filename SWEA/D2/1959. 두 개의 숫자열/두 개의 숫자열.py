T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    total = -float('inf')

    if N <= M:
        short, long = N, M  
        lst1 = list(map(int, input().split()))
        lst2 = list(map(int, input().split()))
    else:
        short, long = M, N
        lst2 = list(map(int, input().split()))
        lst1 = list(map(int, input().split()))

    for i in range(long - short + 1):
        temp = 0
        for j in range(short):
            temp += lst1[j] * lst2[i+j]
        if total <= temp:
            total = temp
    
    print(f"#{test_case} {total}")