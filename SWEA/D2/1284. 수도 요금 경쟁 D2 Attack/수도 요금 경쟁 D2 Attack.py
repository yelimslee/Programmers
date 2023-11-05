T = int(input())
for test_case in range(1, T+1):
    A_pay = 0
    B_pay = 0

    P, Q, R, S, W = map(int, input().split())
    A_pay = P*W
    if W<R:
        B_pay = Q
    else:
        B_pay = Q+(W-R)*S
    if A_pay < B_pay:
        ans = A_pay
    else:
        ans = B_pay
    
    print(f"#{test_case} {ans}")