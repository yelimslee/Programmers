T = int(input())
for test_case in range(1, T+1):
    lst = list(map(int, input().split()))
    mx = max(lst) 
    mn = min(lst)
    avg = round((sum(lst)-mx-mn) / 8)

    print(f"#{test_case} {avg}")