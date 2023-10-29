
T = int(input())
for test_case in range(1, T+1):
    test_case = int(input())
    scores = list(map(int, input().split()))
    score_counts = {}

    for score in scores:
        if score in score_counts:
            score_counts[score] += 1
        else:
            score_counts[score] = 1

    max_count = 0
    mode = 0

    for score, count in score_counts.items():
        if count > max_count or (count == max_count and score > mode):
            max_count = count
            mode = score


    print(f"#{test_case} {mode}")