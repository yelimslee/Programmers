test_case = []
T = int(input())
for i in range(1, T+1):
    n = int(input())

    while(1):
        n = str(n)
        if len(n) == 1:
            test_case.append(n)
            break
        else:
            b = []
            for i in n:
                b.append(int(i))
            n = str(sum(b))
j = 1
for i in test_case:
    print(f"#{j} {i}")
    j += 1