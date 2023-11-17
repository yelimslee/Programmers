T = 10
for test_case in range(1, T+1):
    _ = int(input())
    lst = list(map(int, input().split()))
    while lst[-1] != 0:
        for i in range(1, 6):
            lst.append(lst.pop(0)-i)  # 배열의 첫 번째 값을 꺼낸 후, i만큼 감소시킨 값을 맨 뒤에 추가
            if lst[-1] <= 0:
                lst[-1] = 0
                break
    print(f"#{test_case}", *lst)