T = int(input())  

for test_case in range(1, T + 1):
    h1, m1, h2, m2 = map(int, input().split())

    hour = h1 + h2  
    minute = m1 + m2  

    if minute >= 60:
        hour += 1  
        minute %= 60  
        
    if hour >= 12:
        hour -= 12 

    print(f"#{test_case} {hour} {minute}")
