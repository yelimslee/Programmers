T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    
    cnt_50000 = N // 50000
    N %= 50000
    
    cnt_10000 = N // 10000
    N %= 10000
    
    cnt_5000 = N // 5000
    N %= 5000
    
    cnt_1000 = N // 1000
    N %= 1000
    
    cnt_500 = N // 500
    N %= 500
    
    cnt_100 = N // 100
    N %= 100
    
    cnt_50 = N // 50
    N %= 50
    
    cnt_10 = N // 10
    
    print(f"#{test_case}")
    print(cnt_50000, cnt_10000, cnt_5000, cnt_1000,cnt_500,cnt_100,cnt_50,cnt_10)       