T = int(input())

for test_case in range(1, T + 1):
    N = input()
    value = int(N)
    data = [0] * 10

    while True:
        for j in range(len(N)):
            data[int(N[j])] += 1
        if 0 not in data:
            print(f"#{test_case} {int(N)}")
            break

        N = str(value + int(N))