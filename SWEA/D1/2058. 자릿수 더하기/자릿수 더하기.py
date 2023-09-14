number = list(input())  # list를 통해 값 받기
number = list(map(int, number))  # map으로 정수화하기
sum_number = sum(number)
print(sum_number)