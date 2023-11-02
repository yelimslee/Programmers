T = 10
for test_case in range(1, T+1):
    dump = int(input())
    box = list(map(int, input().split()))

    while dump:
        max_box = max(box)
        min_box = min(box)
        max_idx = box.index(max(box))
        min_idx = box.index(min(box))

        box[max_idx] -= 1
        box[min_idx] += 1

        dump -= 1

    print(f"#{test_case} {max(box) - min(box)}")



# 1. 정렬(오름차순)  2. lst[0]+=1, lst[-1]-=1
T = 10
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    
    for _ in range(N):
        lst.sort()
        lst[0] += 1
        lst[-1] -= 1

    
    print(f"#{test_case} {max(lst)-min(lst)}")
