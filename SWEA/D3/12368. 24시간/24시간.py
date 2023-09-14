def twentyfourhours(test_case, now, hour):
    time = now + hour
    
    return "#" + str(test_case) + " " + str(time % 24)


if __name__ == "__main__":
    T = int(input())

    for test_case in range(1, T + 1):
        now, hour = map(int, input().split())

        print(twentyfourhours(test_case, now, hour))