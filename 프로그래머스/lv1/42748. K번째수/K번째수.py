def solution(array, commands):
    answer = []
    # commands를 순회(for loop)
    for start, end, idx in commands:
       
        arr = array[start -1 : end]
        arr.sort()
        
        answer.append(arr[idx - 1])
    
    return answer