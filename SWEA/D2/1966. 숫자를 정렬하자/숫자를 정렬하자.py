T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    print(f"#{test_case}", end=" ")
    for i in lst:
        print(i, end=" ")
    print()