T = int(input())
for test_case in range(1, T+1):
    a = list(input())
    s = 0  # 마디길이
    ans = 0

    for j in range(1, 10):
        if a[0] != a[j] or a[1] != a[j+1]:
            s += 1
        else:
            break
    ans = s+1    
    print(f"#{test_case} {ans}")