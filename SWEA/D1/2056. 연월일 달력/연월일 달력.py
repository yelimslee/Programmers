T = int(input())
for test_case in range(1, T+1):
    x = str(input())
    year = x[0:4]
    month = x[4:6]
    day = x[6:]
    days = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    fail = -1

    if 0 < int(month) < 13 and int(day) <= days[int(month)]:
        print(f"#{test_case} {year}/{month}/{day}")
    else:
        print(f"#{test_case} {fail}")