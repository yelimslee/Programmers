def solution(numbers):
    # 미리 모든 값을 더한 수를 계산 한 후, 나머지를 빼는 방식
    return 45 - sum(numbers)
    
    # 수를 모두 더하지 않고, 배열에서 직접 제거한 후 더하는 방식
    sumList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    for num in numbers:
        sumList.remove(num)
    return sum(sumList)

# solution = lambda x: 45 - sum(x) 람다식 풀이