N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
answer = numbers[N//2]
print(answer)