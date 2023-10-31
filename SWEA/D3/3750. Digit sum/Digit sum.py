# 재귀함수를 사용하고 테스트케이스 결과 출력 시 하나하나 출력하게 되면 실행시간이 많이 듦
# 따라서 재귀함수 대신 반복문을 사용할 것, 테스트케이스 결과를 한 꺼번에 출력할 것
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





# 시간 초과
T = int(input())
result = []

for test_case in range(1, T + 1):
    n = input()

    while len(n) != 1:
        sum_value = 0  # 각 자릿수의 누적값
        for i in range(len(n)):
            sum_value += int(n[i])
        n = str(sum_value)

    result.append(n)

    print(f"#{test_case} {result[test_case - 1]}")
    # 첫번째 테스트 케이스의 결과는 result[0]에 저장 되므로 test_case -1 을 해야 함
